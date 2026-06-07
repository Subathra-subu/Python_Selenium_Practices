import time
import selenium.webdriver
from selenium.webdriver.common.by import By
import selenium

driver = selenium.webdriver.Chrome()
driver.get("https://letcode.in/frame")
driver.maximize_window()
driver.switch_to.frame("firstFr")
driver.find_element(By.NAME,"fname").send_keys("Suba")
driver.find_element(By.NAME,"lname").send_keys("thra")

inner_frame = driver.find_element(By.XPATH,"//iframe[@src='innerframe']")
driver.switch_to.frame(inner_frame)
driver.find_element(By.NAME,"email").send_keys("suba@gmail.com")
driver.switch_to.parent_frame()
driver.find_element(By.NAME,"fname").clear()
driver.find_element(By.NAME,"fname").send_keys("Karthika")
driver.find_element(By.NAME,"lname").clear()
driver.find_element(By.NAME,"lname").send_keys("V")
time.sleep(5)