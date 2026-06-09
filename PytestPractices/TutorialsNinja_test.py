from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import conftest
import read_config

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_validproduct(self):
        validsearch = read_config.get_config("Search term","validterm")
        self.driver.find_element(By.NAME, "search").send_keys(validsearch)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()


    def test_invalidproduct(self):
        invalidsearch = read_config.get_config("Search term","invalidterm")
        self.driver.find_element(By.NAME, "search").send_keys(invalidsearch)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        expected = "There is no product that matches the search criteria."
        actual = self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text
        assert actual == expected


    def test_noproduct(self):
        self.driver.find_element(By.NAME, "search").send_keys("")
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        expected = "There is no product that matches the search criteria."
        actual = self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text
        assert actual == expected