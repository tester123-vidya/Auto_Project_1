"""
xpath revision:
https://tutorialsninja.com/demo/
Scenario1: My Account Registration with mandatory fields
Account got registered properly
email: Rama_Rao@gmail.com
Password: Rama@123

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_reg_mandatoryfields:

    def test_reg_1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://tutorialsninja.com/demo/")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,value="//span[text()='My Account']").click()
        driver.find_element(By.XPATH,value="//a[text()='Register']").click()

        RegisterAccount = driver.find_element(By.XPATH,"//h1[text()='Register Account']")
        assert RegisterAccount.is_displayed()
        print("Register Account Page Opened Successfully")

        driver.find_element(By.XPATH,"//input[@id='input-firstname']").send_keys("Rama")
        driver.find_element(By.XPATH,"//input[@id='input-lastname']").send_keys("Rao")
        driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("Rama_Rao@gmail.com")
        driver.find_element(By.XPATH,"//input[@id='input-telephone']").send_keys(1234567890)
        driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("Rama@123")
        driver.find_element(By.XPATH,"//input[@id='input-confirm']").send_keys("Rama@123")

        subscribe = driver.find_element(By.XPATH,"//input[@value='0'and @checked ='checked']")
        assert subscribe.is_selected()

        driver.find_element(By.XPATH,"//input[@type='checkbox' and @name='agree']").click()
        driver.find_element(By.XPATH,"//input[@type='submit'and @class='btn btn-primary']").click()
        time.sleep(30)



