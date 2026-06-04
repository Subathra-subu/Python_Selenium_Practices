from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)
driver.get("http://automationexercise.com")
time.sleep(5)
print(driver.title)
home = driver.find_element(By.XPATH, value="//li/a[text()=' Home']")
assert home.is_displayed()
login_btn = driver.find_element(By.XPATH, "//ul[@class='nav navbar-nav']/child::li[4]")
login_btn.click()

new_user_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='signup-form']/h2"))).text
assert new_user_text == "New User Signup!"
driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("Mylambigai")
driver.find_element(By.XPATH, "//input[@placeholder='Name']//following-sibling::input[@placeholder='Email Address']").send_keys("2k22ece056@kiot.ac.in")
driver.find_element(By.XPATH, "//button[@type='submit'][text()='Signup']").click()
driver.find_element(By.XPATH, "//div[@class='login-form']/h2/b").is_displayed()

#Form filling
driver.find_element(By.XPATH, "//input[@value='Mrs']").click()
driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("123456")
day = driver.find_element(By.XPATH, "//select[@id='days']")
opts = Select(day)
opts.select_by_visible_text("16")
month = driver.find_element(By.XPATH, "//select[@id='months']")
opts2 = Select(month)
opts2.select_by_visible_text("May")
year = driver.find_element(By.XPATH, "//select[@id='years']")
opts3 = Select(year)
opts3.select_by_visible_text("2005") 

driver.find_element(By.XPATH, "//input[@id='newsletter']").click()
driver.find_element(By.XPATH, "//input[@id='optin']").click()

driver.find_element(By.XPATH,"//input[@id='first_name']").send_keys("Myl")
driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("G")
driver.find_element(By.XPATH, "//input[@id='address1']").send_keys("115/2, KN patty, salem")
driver.find_element(By.CSS_SELECTOR, "input[id='state']").send_keys("Tamil nadu")
driver.find_element(By.CSS_SELECTOR, "input[id='city']").send_keys("Salem")
driver.find_element(By.CSS_SELECTOR, "input[id='zipcode']").send_keys("636008")
driver.find_element(By.ID, "mobile_number").send_keys("3216540897")
driver.find_element(By.XPATH, "//button[text()='Create Account']").click()
acc_created = driver.find_element(By.XPATH, "//div/h2/b").text
print(acc_created)
assert acc_created.lower() == "account created!"
driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()
print(driver.current_url)
user_loggedIn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]"))).text
print(user_loggedIn)
driver.find_element(By.XPATH, "//a[normalize-space()='Delete Account']").click()
acc_delete = driver.find_element(By.XPATH, "//b[normalize-space()='Account Deleted!']").text
print(acc_delete)
assert acc_delete.lower() == "account deleted!"
driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()

driver.close()