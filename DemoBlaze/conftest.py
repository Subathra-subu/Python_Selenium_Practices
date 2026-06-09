import selenium
from selenium import webdriver
import read_config
import pytest

@pytest.fixture()
def setup_and_teardown(request):
    browser = read_config.get_config("basic info","browser")
    if browser == "Chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(5)
    url = read_config.get_config("basic info","url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()