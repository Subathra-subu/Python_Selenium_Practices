from selenium.webdriver.common.by import By
import Utilities.logCreater

class HomePage:
    
    logger = Utilities.logCreater.log_creator()
    
    def __init__(self,driver):
        self.driver = driver
    
    search_box_field = "search"
    search_button = "//button[contains(@class,'btn-default')]"
    desktop = "//a[text()='Desktops']"
    showAllDesktops = "//a[text()='Show AllDesktops']"
    dropdown = "//span[@class='caret']"
    loginlink = "//a[text()='Login']"
    
    def search_action(self,search):
        self.driver.find_element(By.NAME,self.search_box_field).send_keys(search)
        self.logger.info("Search item entered")
        self.driver.find_element(By.XPATH,self.search_button).click()
        self.logger.info("Search button clicked")
    
    def  click_desktop(self):
        self.driver.find_element(By.XPATH,self.desktop).click()
        self.logger.info("Desktop link clicked")
        self.driver.find_element(By.XPATH,self.showAllDesktops).click()
        self.logger.info("Show All desktop link clicked")
        
    def click_DropDown(self):
        self.driver.find_element(By.XPATH,self.dropdown).click()
        self.logger.info("Dropdown clicked")
        
    def click_Loginlink(self):
        self.driver.find_element(By.XPATH,self.loginlink).click()
        self.logger.info("Login link clicked")
        
