from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()
driver.implicitly_wait(10)

homepage = driver.find_element(By.XPATH,"//a[normalize-space()='Home']")
if homepage.is_displayed():
    print("HomePage is visible")
else:
    print("HomePage is not visible")
    
element = driver.find_element(By.XPATH, "//a[contains(text(),'Test Cases')]")
driver.execute_script("arguments[0].click();", element)
testcases = driver.find_element(By.XPATH,"//b[normalize-space()='Test Cases']").text

assert testcases == "TEST CASES"
print("Test cases page is visible")