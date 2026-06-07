import time
import selenium.webdriver
from selenium.webdriver.common.by import By
import selenium


driver = selenium.webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")

parent_tab = driver.current_window_handle

driver.find_element(By.XPATH,"//button[@id='tabButton']").click()

opened_tabs = driver.window_handles

driver.switch_to.window(opened_tabs[1])

print(driver.find_element(By.TAG_NAME,"h1").text)

driver.switch_to.window(opened_tabs[0])

print(parent_tab == driver.current_window_handle)