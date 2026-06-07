import time
import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


driver = selenium.webdriver.Chrome()
driver.get("https://www.leafground.com/drag.xhtml")
driver.maximize_window()

actions = ActionChains(driver)

image = driver.find_element(By.XPATH,"//div[@class='ui-wrapper']")
actions.scroll_to_element(image).perform()

time.sleep(5)

target = driver.find_element(By.XPATH,"//div[@id='form:drag_content']")
actions.move_to_element(target).perform()

drop = driver.find_element(By.XPATH,"//div[@id='form:drop_content']")

actions.drag_and_drop(target,drop).perform()

range_slider = driver.find_element(By.XPATH,"(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[1]")

origin = ScrollOrigin.from_viewport(0, 0)
actions.scroll_from_origin(origin, 0, 700).perform()

actions.drag_and_drop_by_offset(range_slider,200,0).perform()

time.sleep(5)