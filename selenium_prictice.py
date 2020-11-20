# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Select all next button


url = "https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/"
driver = webdriver.Chrome('Driver/chromedriver.exe')
driver.get(url)
# import time
# time.sleep(3)
#
# try:
#     # get element
#     element = driver.find_element_by_link_text("next")
#
#     # click the element
#     element.click()
#
#     new_link = driver.current_url
#
#     if new_link != url:
#         time.sleep(3)
#         element.click()
#
# except:
#     print('No page found')
#



path = "//th[normalize-space() = 'ASIN']//following-sibling::td"
path1 = '//table[@id="productDetails_detailBullets_sections1"]/tbody/tr[4]/td/span/span'
path2 = '//table[@id="productDetails_detailBullets_sections1"]/tbody/tr[4]/td/span/span[2]'

element = driver.find_element_by_xpath(path1)
ee = driver.find_element_by_xpath(path2)
print(element.text)
print(ee.text)

driver.quit()