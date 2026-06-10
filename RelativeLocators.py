import selenium 
import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import time

driver = selenium.webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.hyrtutorials.com/p/add-padding-to-containers.html")

email = driver.find_element(By.XPATH,"//label[text()='Email']/following-sibling::input[1]");
email.send_keys("Sham@yahoo.com")

last_name = driver.find_element(locate_with(By.TAG_NAME,"input").above(email))
last_name.send_keys("Davis")

password = driver.find_element(locate_with(By.TAG_NAME,"input").below(email))
password.send_keys("12345")

clear_button = driver.find_element(By.XPATH,"//div[@class='buttons']/child::button[@type='reset'][1]")

register_button = driver.find_element(locate_with(By.TAG_NAME,"button").to_left_of(clear_button)).click()

time.sleep(5)

reset_button = driver.find_element(By.XPATH,"//div[@class='buttons']/child::button[@type='reset'][2]")

time.sleep(5)

refresh_button = driver.find_element(locate_with(By.TAG_NAME,"button").to_right_of(reset_button)).click()

time.sleep(5)

driver.find_element(locate_with(By.TAG_NAME,"button").near(reset_button)).click()



