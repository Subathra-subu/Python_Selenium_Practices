from selenium.webdriver.common.by import By

class SearchPage:
    
    def __init__(self,driver):
        self.driver = driver
        
        
    display_status = "HP LP3065"
    
    def display_status_valid_search(self):
        return self.driver.find_element(By.LINK_TEXT,self.display_status).is_displayed()