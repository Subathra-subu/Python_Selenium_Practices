from ast import arguments
import time
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


driver = selenium.webdriver.Chrome()
driver.get("https://automationexercise.com/")

wait = WebDriverWait(driver, 10)

driver.maximize_window()

assert driver.title == "Automation Exercise"
print("Home page was launched")

driver.find_element(By.XPATH,value="//a[text()=' Signup / Login']").click()

login_page = driver.find_element(By.XPATH,value="//div[@class='login-form']/child::h2")

login_page_text=wait.until(ec.visibility_of(login_page))

if login_page_text.__eq__("Login to your account"):
    print("Login section was displayed")
else:
    print("Login section was not displayed")

driver.find_element(By.XPATH,value="//form[@action='/login']/child::input[2]").send_keys("charu@gmail.com")

driver.find_element(By.XPATH,value="//form[@action='/login']/child::input[3]").send_keys("1234")

login = driver.find_element(By.XPATH,value="//form[@action='/login']/child::button")

driver.execute_script("arguments[0].click();",login)

logged_in = driver.find_element(By.XPATH,value="//ul[@class='nav navbar-nav']/child::*[10]")

wait.until(ec.visibility_of(logged_in))

print("Logged in successfully")

driver.find_element(By.XPATH,value="//a[text()=' Logout']").click()

WebDriverWait(driver, 10).until(ec.url_to_be("https://automationexercise.com/login"))

url = driver.current_url
assert url.__eq__("https://automationexercise.com/login")
print("Logout successfull")

driver.close()

