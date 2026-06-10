import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import read_config
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import Utilities.logCreater

@pytest.mark.usefixtures("setup_and_teardown")
class Testlogin:
    logger = Utilities.logCreater.log_creator()
    def test_validLogin(self):
        email = read_config.get_data("Login credentials","email")
        password = read_config.get_data("Login credentials","password")
        
        self.driver.find_element(By.XPATH,"//span[@class='caret']").click()
        self.logger.info("Dropdown clicked")
        self.driver.find_element(By.XPATH,"//a[text()='Login']").click()
        self.logger.info("Login link clicked")
        self.driver.find_element(By.XPATH,"(//div[@class='form-group'])[1]/child::input").send_keys(email)
        self.logger.info("Eamil entered")
        self.driver.find_element(By.XPATH,"(//div[@class='form-group'])[2]/child::input").send_keys(password)
        self.logger.info("Password entered")
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        self.logger.info("Login button clicked")
        assert self.driver.find_element(By.XPATH,"//h2[text()='My Account']").is_displayed()
        self.logger.info("Login successfull")
        
        