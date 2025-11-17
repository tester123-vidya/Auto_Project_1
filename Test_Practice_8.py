"""
xpath revision:
https://tutorialsninja.com/demo/
Scenario2: Login to the registered account
email: Rama_Rao@gmail.com
Password: Rama@123
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_login:

    def test_login_validation(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://tutorialsninja.com/demo/")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,"//span[text()='My Account']" ).click()
        driver.find_element(By.LINK_TEXT,"Login").click()
        time.sleep(10)

        driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("Rama_Rao@gmail.com")
        driver.find_element(By.XPATH,value="//input[@id='input-password']").send_keys("Rama@123")
        driver.find_element(By.XPATH,value="//input[@class='btn btn-primary']").click()

        Login_Success = driver.find_element(By.XPATH,"//h2[text()='My Account']")
        assert Login_Success.is_displayed()
        print("Login Successful")