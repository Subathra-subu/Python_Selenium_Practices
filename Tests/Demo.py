import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()

actual_title = driver.title
if(actual_title=="Google"):
    print("Google launched successfully")
else:
    print("Not correct website")
time.sleep(5)
element = driver.find_element( By.NAME, value="q")

if element.is_displayed():
    element.send_keys("Selenium")
else:
    print("Element is not displayed")

time.sleep(5)
button = driver.find_element(By.NAME, value="btnK")

if button.is_enabled():
    button.click()
    print("Button clicked")
else:
    print("Button is not displayed")
time.sleep(5)

driver.close
