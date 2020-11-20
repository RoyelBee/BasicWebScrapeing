# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# Select all next button


import pandas as pd

linkdf = pd.read_excel('LinkDataset/Amazon_UPC.xlsx')

upc_list = linkdf['UPC'].tolist()

baseurl = 'https://www.amazon.com/dp/'
extension = '?th=1'

title_l = []
price_l = []
asin_l = []
rating_l = []
best_seller1_l = []
best_seller2_l = []

for url in range(len(upc_list)):
    url = baseurl + upc_list[url] + extension

    try:
        driver = webdriver.Chrome('Driver/chromedriver.exe')
        driver.get(url)
        import time

        time.sleep(5)


        # title = driver.find_element_by_id('productTitle')
        # price = driver.find_element_by_class_name('a-color-price')
        # rating = driver.find_element_by_xpath('//table/tbody/tr[3]/td')

        def get_rating():
            try:
                rating = driver.find_element_by_xpath('//div[@id="reviewsMedley"]/div/div/div/div/div/div/div/span/span')
                rating = rating.text
            except AttributeError:
                rating = ''

            return rating


        def get_asin():
            try:
                asin = driver.find_element_by_xpath('//table[@id="productDetails_detailBullets_sections1"]/tbody/tr/td')
                asin = asin.text
            except AttributeError:
                asin = ''
            return asin


        def get_title():
            try:
                title = driver.find_element_by_id('productTitle')
                title = title.text
            except AttributeError:
                title = ''
            return title


        def get_price():
            try:
                price = driver.find_element_by_class_name('a-color-price')
                price = price.text
            except AttributeError:
                price = ''
            return price


        def get_bs_rating1():
            try:
                bestseller1 = driver.find_element_by_xpath('//span/span[contains(text(), "#")]')

                bestseller1 = bestseller1.text
            except:
                bestseller1 = ''
            return bestseller1


        def get_bs_rating2():
            try:
                bestseller2 = driver.find_element_by_xpath('//span/span[2][contains(text(), "#")]')

                bestseller2 = bestseller2.text
            except:
                bestseller2 = ''
            return bestseller2


        print('ASIN          = ', get_asin())
        # print('Title         = ', get_title())
        # print('Price         = ', get_price())
        # # print('Rating        = ', get_rating())
        # print('Best Seller 1 = ', get_bs_rating1())
        # print('Best Seller 2 = ', get_bs_rating2())
        # print('')

        asin_l.append(get_asin())
        title_l.append(get_title())
        price_l.append(get_price())
        # rating_l.append()
        best_seller1_l.append(get_bs_rating1())
        best_seller2_l.append(get_bs_rating2())

        driver.quit()
    except:
        continue

print(asin_l)

df = pd.DataFrame()
df['ASIN'] = asin_l
df['Title'] = title_l
df['Price'] = price_l
df['Best Seller 1'] = best_seller1_l
df['Best Seller 2'] = best_seller2_l

df.to_excel('Data/AmazonProductDataset.xlsx', index=False)

