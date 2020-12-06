# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# # ----------------------------------------
# # -------- Part 01 -----------------------
# # ----------------------------------------
import time

url = "https://www.ups.com/track?loc=en_US&requester=ST/"
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

# # Set Key
search_input = driver.find_element_by_id("stApp_trackingNumber")
search_input.send_keys("1Z7A801T3535584776")
search_btn = driver.find_element_by_id("stApp_btnTrack")
search_btn.click()

time.sleep(5)

status = driver.find_element_by_id("stApp_lblDeliveredDate")
day = driver.find_element_by_id("stApp_deliveredDay")
date = driver.find_element_by_id("stApp_deliveredDate")
time = driver.find_element_by_id("stApp_eodDate")
deliveredTo = driver.find_element_by_id("stApp_txtAddress")
deliveredToCountry = driver.find_element_by_id("stApp_txtCountry")
leftAt = driver.find_element_by_id("stApp_txtLeftAt")
received_by = driver.find_element_by_id("stApp_txtReceivedBy")

print(status.text)
print(day.text)
print(date.text)
print(time.text)
print(deliveredTo.text)
print(deliveredToCountry.text)
print(leftAt.text.split()[2])
print(received_by.text.split()[2, 3])

driver.quit()
