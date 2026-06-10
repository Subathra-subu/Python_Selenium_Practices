from turtle import home

import pytest
from Pages.DesktopPage import DesktopPage
from Pages.IphonePage import IphonePage
from Pages.HomePage import HomePage

@pytest.mark.usefixtures("setup_and_teardown")
class TestPriceRetrieval:
    
    def test_PrintPrice(self):
        homePage = HomePage(self.driver)
        desktopPage = DesktopPage(self.driver)
        iphonePage = IphonePage(self.driver)
        
        homePage.click_desktop()
        desktopPage.clickIphoneImage()
        print("Price of IPhone: ",iphonePage.getPrice)