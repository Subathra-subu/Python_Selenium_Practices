import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")

driver.maximize_window()

if driver.title == "Automation Exercise":
    print("Home page was launched")
else:
    print("Home page was not launched")

driver.find_element(By.XPATH,value="//a[text()=' Signup / Login']").click()

signup_page = driver.find_element(By.XPATH,value="//div[@class='signup-form']/child::h2").text

if signup_page.__eq__("New User Signup!"):
    print("Signup section was displayed")
else:
    print("Signup section was not displayed")

driver.find_element(By.XPATH,value="//div[@class='signup-form']/child::form/child::input[2]").send_keys("Emily")
driver.find_element(By.XPATH,value="//div[@class='signup-form']/child::form/child::input[3]").send_keys("emily@gmail.com")
driver.find_element(By.XPATH,value="//div[@class='signup-form']/child::form/child::button").click()



driver.find_element(By.XPATH,value="//input[@value='Mrs']").click()
