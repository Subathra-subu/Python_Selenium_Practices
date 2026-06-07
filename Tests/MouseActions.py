import selenium.webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = selenium.webdriver.Chrome()
driver.get("https://automationexercise.com/")
wait = WebDriverWait(driver,10)

actions = ActionChains(driver)

driver.maximize_window()

assert driver.title == "Automation Exercise"
print("Home page was launched")

product = driver.find_element(By.XPATH,"//a[text()=' Products']")
actions.click(product).perform()
productname=[]

actions.move_to_element(driver.find_element(By.XPATH,"(//div[@class='product-image-wrapper'])[1]")).perform()
productname.append((driver.find_element(By.XPATH,"(//div[@class='productinfo text-center']/child::p)[1]")).text)
actions.click(driver.find_element(By.XPATH,"(//a[@data-product-id='1'])[2]")).perform()

continue_button = wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Continue Shopping']")))
continue_button.click()

actions.move_to_element(driver.find_element(By.XPATH,"(//div[@class='product-image-wrapper'])[2]")).perform()
productname.append((driver.find_element(By.XPATH,"(//div[@class='productinfo text-center']/child::p)[2]")).text)
actions.click(driver.find_element(By.XPATH,"(//a[@data-product-id='2'])[2]")).perform()

view_cart = wait.until(ec.element_to_be_clickable((By.XPATH, "//u[text()='View Cart']")))
view_cart.click()

cart_products = driver.find_elements(By.XPATH,"//table//tr//td[2]//a").text

for i in productname:
    found = False
    if i in cart_products:
        found=True

    if found: continue
    else: break
else: print("Products added successfully")
print(cart_products)