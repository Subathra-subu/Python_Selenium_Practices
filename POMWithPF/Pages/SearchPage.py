from seleniumpagefactory.Pagefactory import PageFactory

class SearchPage(PageFactory):
    
    def __init__(self,driver):
        self.driver = driver
        
        
    locators={'display_status': ("Link_Text","HP LP3065")}
    
    def display_status_valid_search(self):
        return self.display_status.get_text