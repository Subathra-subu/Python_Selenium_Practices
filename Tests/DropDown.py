import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

d=webdriver.Chrome()
d.maximize_window()
d.get("https://leafground.com/select.xhtml;jsessionid=node075rumjteenlg1jb92qjgb622z17897253.node0")
drop=d.find_element(By.XPATH,"//select[@class='ui-selectonemenu']")
sec=Select(drop)
sec.select_by_visible_text("Selenium")
l=sec.options
for i in l:
    print(i.text)
sec.select_by_visible_text("Playwright")
k=sec.all_selected_options
for i in k:
    print(i.text)
time.sleep(10)