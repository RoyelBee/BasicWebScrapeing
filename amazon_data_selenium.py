# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# Select all next button

from bs4 import BeautifulSoup
import pandas as pd
import requests

linkdf = pd.read_excel('LinkDataset/Amazon_UPC - Copy.xlsx')

upc_list = linkdf['UPC'].tolist()

baseurl = 'https://www.amazon.com/dp/'
extension = '?th=1'

title_l = []
price_l = []
asin_l = []
rating_l = []
best_seller1_l = []
best_seller2_l = []
review_qty = []
all_rat = []
all_rev = []

for url in range(len(upc_list)):
    url = baseurl + upc_list[url] + extension
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

    try:
        driver = webdriver.Chrome('../Scrapy/chromedriver.exe')
        driver.get(url)
        import time

        time.sleep(5)


        # title = driver.find_element_by_id('productTitle')
        # price = driver.find_element_by_class_name('a-color-price')
        # rating = driver.find_element_by_xpath('//table/tbody/tr[3]/td')

        def get_rating():
            try:
                rating = driver.find_element_by_xpath(
                    '//div[@id="reviewsMedley"]/div/div/div/div/div/div/div/span/span')
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

                bestseller1 = bestseller1.text.split()[0]
            except:
                bestseller1 = ''
            return bestseller1


        def get_bs_rating2():
            try:
                bestseller2 = driver.find_element_by_xpath('//span/span[2][contains(text(), "#")]')

                bestseller2 = bestseller2.text.split()[0]
            except:
                bestseller2 = ''
            return bestseller2


        def all_reviews():

            try:
                a = []
                ids = driver.find_elements_by_xpath('//div[@class="a-section celwidget"]/div[4]/span/div/div/span')
                for ii in ids:
                    a.append(ii.text)  # id name as string

            except:
                a = ''
            return a

        def reviews_qtys():

            try:
                b = []
                ids = driver.find_elements_by_xpath('//div[@class="a-section celwidget"]/div[4]/span/div/div/span')
                b = len(ids)

            except:
                b = ''
            return b


        def all_ratings():
            try:
                r = []
                rat = driver.find_elements_by_xpath('//div[@class="a-section celwidget"]/div[2]/a/i/span[@class="a-icon-alt"]')
                for ii in rat:
                    r.append(ii.text)


            except:
                r = ''
            return r


        def test():
            try:
                rat = driver.find_element_by_xpath('//*[@id="cm-cr-local-reviews-title"]/h3/text()')

                rat = rat
            except:
                rat = ''
            return rat


        print('ASIN          = ', get_asin())
        # print('Title         = ', get_title())
        # print('Price         = ', get_price())
        print('Rating        = ', get_rating())
        # print('Best Seller 1 = ', get_bs_rating1())
        # print('Best Seller 2 = ', get_bs_rating2())

        asin_l.append(get_asin())
        title_l.append(get_title())
        price_l.append(get_price())
        best_seller1_l.append(get_bs_rating1())
        best_seller2_l.append(get_bs_rating2())
        review_qty.append(reviews_qtys())
        all_rat.append(all_ratings())
        all_rev.append(all_reviews())

        driver.quit()
    except:
        continue

print(all_rat)

df = pd.DataFrame()
df['ASIN'] = asin_l
df['Title'] = title_l
df['Price'] = price_l
df['Best Seller 1'] = best_seller1_l
df['Best Seller 2'] = best_seller2_l
df['Review QTY'] = review_qty
df['All Ratings'] = all_rat
df['all reviwes'] = all_rev

df.to_excel('Data/a.xlsx', index=False)
