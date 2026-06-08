from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.leafground.com/select.xhtml")

dropdown = driver.find_element( By.XPATH, "//select[@class='ui-selectonemenu']")
select = Select(dropdown)
 
select.select_by_index(1)
print("Selected:", select.first_selected_option.text)
time.sleep(5) 
select.select_by_index(2)
print("Selected:", select.first_selected_option.text)

time.sleep(5)
driver.quit()