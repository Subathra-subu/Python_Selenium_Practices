from selenium.webdriver.common.by import By
from POMWithoutPF import read_config
import Utilities.logCreater

logger = Utilities.logCreater.log_creator()

class HomePage:
    
    def __init__(self,driver):
        self.driver = driver
        
    email = "(//div[@class='form-group'])[1]/child::input"
    password = "(//div[@class='form-group'])[2]/child::input"
        
    
    def enter_credentials(self): 
        useremail = read_config.get_data("login credentials","email")
        self.driver.find_element(By.XPATH,self.email).send_keys(useremail)
        self.logger.info("Email entered")
        userpassword = read_config.get_data("login credentials","password")
        self.driver.find_element(By.XPATH,self.password).send_keys(userpassword)
        self.logger.info("Password entered")
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        self.logger.info("Login button clicked")