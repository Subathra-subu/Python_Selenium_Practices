import pytest
from Pages.HomePage import HomePage
from Pages.SearchPage import SearchPage

@pytest.mark.usefixtures("setup_and_teardown")

class TestSearch:
    
    def test_validproduct(self):
        homepage = HomePage(self.driver)
        homepage.enter_product("HP")
        homepage.click_search_button()
        searchpage = SearchPage(self.driver)
        assert searchpage.display_status_valid_search()