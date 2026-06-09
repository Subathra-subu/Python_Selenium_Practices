from tabnanny import check

from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time
import pytest_check as check

def setup_function(function):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
    
def teardown_function(function):
    driver.quit()
   
@pytest.mark.order(2) 
def test_validproduct():
    driver.find_element(By.NAME, "search").send_keys("HP")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    check(driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed())

@pytest.mark.order(3) 
def test_invalidproduct():
    driver.find_element(By.NAME, "search").send_keys("Honda")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    expected = "There is no product that matches the search criteria."
    actual = driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text
    check.equal(actual,expected) 


def test_noproduct():
    driver.find_element(By.NAME, "search").send_keys("")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    expected = "There is no product that matches the search criteria."
    actual = driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text
    check.equal(actual,expected)