from seleniumpagefactory.Pagefactory import PageFactory
import Utilities.logCreater

logger = Utilities.logCreater.log_creator()

class HomePage(PageFactory):
    
    def __init__(self,driver):
        self.driver = driver
    
    locators={"search_box_field" :("NAME","search"),"search_button" :("XPATH","//button[contains(@class,'btn-default')]")}
    
    def enter_product(self,product_name):
        self.search_box_field.send_keys(product_name)
        logger.info("Search item entered")
    
    def click_search_button(self):
        self.search_button.click()
        logger.info("Search button clicked")