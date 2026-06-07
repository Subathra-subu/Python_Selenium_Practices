import time
import selenium.webdriver
from selenium.webdriver.common.by import By
import selenium


driver = selenium.webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")

parent_window = driver.current_window_handle

print(parent_window)

driver.find_element(By.XPATH,"//button[@id='windowButton']").click()

child_window = driver.window_handles

print(child_window)

for i in child_window:
    if i!= parent_window:
        driver.switch_to.window(i)

print(driver.find_element(By.TAG_NAME,"h1").text)

driver.switch_to.window(parent_window)

print(driver.current_window_handle)