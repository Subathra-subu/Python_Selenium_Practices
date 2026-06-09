from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import conftest
import read_config
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    
    def test_login(self):
        self.driver.find_element(By.ID,"login2").click()
        uname = read_config.get_config("login credentials","uname")
        password = read_config.get_config("login credentials","password")
        self.driver.find_element(By.ID,"loginusername").send_keys(uname)
        self.driver.find_element(By.ID,"loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH,"//button[text()='Log in']").click()

        wait = WebDriverWait(self.driver,10)
        
        wait.until(ec.visibility_of_element_located((By.ID, "logout2")))
        logout = self.driver.find_element(By.ID,"logout2")
        assert logout.text == "Log out"
        print("Login successfull...")