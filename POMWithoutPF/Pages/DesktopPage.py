from selenium.webdriver.common.by import By
import Utilities.logCreater

logger = Utilities.logCreater.log_creator()

class DesktopPage:
    
    def __init__(self,driver):
        self.driver = driver
        
    iphone_img = "//img[@title='iPhone']"
    
    def clickIphoneImage(self):
        self.driver.find_element(By.XPATH,self.iphone_img).click()
        logger.info("Iphone image clicked")
    
    
