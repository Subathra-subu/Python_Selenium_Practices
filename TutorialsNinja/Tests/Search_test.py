import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import excelReader
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import Utilities.logCreater


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_validproduct(self):
        validsearch = excelReader.get_data("TestData/SearchData.xlsx","Search")
        search_term = validsearch[0]
        self.driver.find_element(By.NAME, "search").send_keys(search_term)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()


    def test_invalidproduct(self):
        invalidsearch = excelReader.get_data("TestData/SearchData.xlsx","Search")
        search_term = invalidsearch[1]
        self.driver.find_element(By.NAME, "search").send_keys(search_term)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        expected = "There is no product that matches the search criteria."
        actual = self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text
        assert actual == expected
