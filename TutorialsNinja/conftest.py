import selenium
from selenium import webdriver
from Utilities import read_config
import pytest
import Utilities.logCreater

@pytest.fixture()
def setup_and_teardown(request):
    logger = Utilities.logCreater.log_creator()
    browser = read_config.get_data("basic info","browser")
    if browser=="Chrome":
        driver = webdriver.Chrome()
    elif browser=="Edge":
        driver = webdriver.Edge()
    elif browser=="Firefox":
        driver = webdriver.Firefox()
    logger.info("Browser launched")
    driver.maximize_window()

    url = read_config.get_data("basic info","url")
    driver.get(url)
    logger.info("Application launched")
    request.cls.driver = driver
    
    yield
    
    driver.quit()