import csv
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=bootcamp+bodyweight")

user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for i in user_data:
    links.append(i.get_attribute('href'))

print(len(links))
df = pd.DataFrame(columns = ['link', 'title', 'description', 'category'])

wait = WebDriverWait(driver, 20)
v_category = "Bootcamp Bodyweight"
for x in links:
        driver.get(x)
        v_id = x.strip('https://www.youtube.com/watch?v=')
        v_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
        v_description = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#description yt-formatted-string"))).text
        length = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span.ytp-time-duration"))).text
        creator = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a.yt-simple-endpoint.style-scope.yt-formatted-string"))).text
        dateOfUpload = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#date yt-formatted-string"))).text
        numberOfLike = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a.yt-simple-endpoint.style-scope.ytd-toggle-button-renderer yt-formatted-string"))).text
        numberOfView = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span.view-count.style-scope.yt-view-count-renderer"))).text
        df.loc[len(df)] = [v_id, v_title, v_description, v_category]
        url = 'https://www.youtube.com/watch?v='+v_id
        with open('ab.csv', 'a+') as f:
                fieldnames = ['Link', 'Category', 'Length', 'Creator', 'Date of Upload', 'Number of Views', 'Number of Likes']
                the_writer = csv.DictWriter(f, fieldnames=fieldnames)

                the_writer.writeheader()
                #for i in range(len(links)):
                the_writer.writerow({'Link': url, 'Category': v_category, 'Length': length, 'Creator': creator, 'Date of Upload': dateOfUpload, 'Number of Views': numberOfView, 'Number of Likes': numberOfLike})