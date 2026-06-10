from selenium.webdriver.common.by import By
import Utilities.logCreater

logger = Utilities.logCreater.log_creator()

class IphonePage:
    
    def __init__(self,driver):
        self.driver = driver
        
    iphone_price= "(//ul[@class='list-unstyled'])[9]/child::li/h2"
    
    def getPrice(self):
        return self.driver.find_element(By.XPATH,self.iphone_price).text
    
    
