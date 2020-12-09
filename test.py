# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time

url = "https://www.fedex.com/apps/fedextrack/?action=track&cntry_code=us&tracknumber_list=399615159111&language=english#"
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

# # Set Key
search_input = driver.find_element_by_id("track_inbox_track_numbers_area")
search_input.send_keys("399615159111")
search_btn = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/form/div[1]/div/button')
search_btn.click()

time.sleep(5)


driver.quit()
