import selenium
from selenium import webdriver
from Utilities import read_config
import pytest

@pytest.fixture()
def setup_and_teardown(request):
    browser = read_config.get_data("basic info","browser")
    if browser=="Chrome":
        driver = webdriver.Chrome()
    elif browser=="Edge":
        driver = webdriver.Edge()
    elif browser=="Firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()

    url = read_config.get_data("basic info","url")
    driver.get(url)
    request.cls.driver = driver
    
    yield
    
    driver.quit()