from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():
    # Update login detail at here
    student_login_email = "xxxxx@student.usm.my"
    student_password = "xxxxx"

    # set notification number at here
    # format: 60123456789 (no - and +)
    user = ['6016xxxXXXX','6016xxxXXXX','6018xxxXXXX']

    # message content, space will be replace by %20
    msgbody = "XXXX XXX XXX"

    # WARNING!
    # need to login whatsapp for once at least.
    # this logon session will take focus of whatsapp session
    options = webdriver.ChromeOptions();
    options.add_argument('--user-data-dir=./User_Data')
    driver = webdriver.Chrome(chrome_options=options)

    # Flag for result record found, default=True
    resFound = True

    driver.get('https://campusonline.usm.my/')
    driver.find_element_by_xpath('//*[@id="header"]/div/div/div/a/img').click();
        
    try:
        driver.find_element_by_xpath('//*[@id="userNameInput"]').send_keys(student_login_email)
        driver.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(student_password)

        driver.find_element_by_xpath('//*[@id="submitButton"]').click()
    except:
        print("no need login")

    # redirect to semgred for sem1
    driver.get('https://campusonline-ver2.usm.my/smup/academic/semgred/181-1')

    quotation_element = driver.find_element_by_xpath('//*[@id="listKursus"]')
    quotation_data = quotation_element.text

    # Process data to array
    data_array = [s.strip() for s in quotation_data.splitlines()]

    # overwrite msgbody at here. can remove this.
    if 'No record' in data_array:
        msgbody = "Hi no record yo"
    else:
        msgbody = "Hi check result yo"

    for user_no in user:
        driver.get('https://api.whatsapp.com/send?phone={}&text={}'.format(user_no,msgbody.replace(' ','%20')))
        driver.find_element_by_xpath('//*[@id="action-button"]').click()
        time.sleep(20) # sleep to let selenium run properly
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(10) # sleep to let messaeg send properly

    # end
    print ("end!")
    driver.close()

# debug only
def loginwhatsapp():
    options = webdriver.ChromeOptions();
    options.add_argument('--user-data-dir=./User_Data')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://web.whatsapp.com/')

main()
