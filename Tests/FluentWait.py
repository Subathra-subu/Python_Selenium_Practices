from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException)

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")

login=driver.find_element(By.XPATH,'//a[@href="/login"]')
login.click()

email=driver.find_element(By.XPATH,'//input[@data-qa="login-email"]')
email.send_keys("queen1@gmail.com")

password=driver.find_element(By.XPATH,'//input[@data-qa="login-password"]')
password.send_keys("1234sho")

loginbtn=driver.find_element(By.XPATH,'//button[@data-qa="login-button"]')
loginbtn.click()

driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()
wait = WebDriverWait(driver,timeout=20,poll_frequency=1,ignored_exceptions=[NoSuchElementException])

login_heading = wait.until( EC.visibility_of_element_located((By.XPATH, "//h2[text()='Login to your account']")))
print("Logout successfully")