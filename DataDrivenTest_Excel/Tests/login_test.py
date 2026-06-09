import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import excelReader
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import Utilities.logcreater

@pytest.mark.parametrize("username,password",excelReader.get_data("ExcelFiles\logindata.xlsx","login"))

class Testlogin:
    
    logger = Utilities.logcreater.log_creator()
    def test_login(self,username,password):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")
        self.logger.info("Application is launched")
        self.driver.find_element(By.ID,"login2").click()
        self.logger.info("Loginlink clicked")
        wait = WebDriverWait(self.driver, 10)
        username_box = wait.until(ec.visibility_of_element_located((By.ID, "loginusername")))
        username_box.send_keys(username)
        self.logger.info("Username entered")
        self.driver.find_element(By.ID,"loginpassword").send_keys(password)
        self.logger.info("Password entered")
        self.driver.find_element(By.XPATH,"//button[text()='Log in']").click()
        self.logger.info("Login button clicked")

        if username=="admin":
            wait = WebDriverWait(self.driver,20)
        
            wait.until(ec.visibility_of_element_located((By.ID, "logout2")))
            logout = self.driver.find_element(By.ID,"logout2")
            assert logout.text == "Log out"
            logout.click()
            self.logger.info("Logout button clicked")
            print("Login successfull...")
        else:
            wait = WebDriverWait(self.driver, 20)
            alert = wait.until(ec.alert_is_present())
            assert alert.text == "Wrong password."
            alert.accept()
            self.logger.info("Alert message continue button clicked")
            print("Login unsuccessfull...")
        self.driver.quit()