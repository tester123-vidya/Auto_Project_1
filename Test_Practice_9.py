"""
xpath with following, preceding,siblings
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
driver.implicitly_wait(10)
