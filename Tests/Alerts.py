from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

#Simple alert 
simple_alert = driver.find_element(By.ID, "alert1")
simple_alert.click()
alert = driver.switch_to.alert
alert.accept()
print("Simple alert is handled!")

#conformation alert
conformation_alert = driver.find_element(By.CSS_SELECTOR, "input[id='confirm']")
conformation_alert.click()
alert = driver.switch_to.alert
alert.dismiss()
print("Conformation alert is handled!")

#Prompt alert
prompt_alert = driver.find_element(By.CSS_SELECTOR, "input[id='prompt']")
prompt_alert.click()
print(alert.text)
alert.send_keys("My name is myl")
alert.accept()
print("Prompt alert is handled!")

driver.close()