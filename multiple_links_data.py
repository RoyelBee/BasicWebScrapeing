import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlrd
import time

links = pd.read_excel('Data/phonelinks.xlsx')
# print(links)

links = links.links.tolist()

phone = []
price = []

for l in range(len(links)):
    link = requests.get(str(links[l])).text
    time.sleep(2)
    soup = BeautifulSoup(link, 'html.parser')

    result = soup.find_all('div', attrs={'class': 'single'})


    for r in result:
        phone.append(r.find(id='name').text)
        price.append(r.find(id="price").text)

df = pd.DataFrame()

df['Phone Name'] = phone
df['Price'] = price

# print(df.head())
df.to_csv('Data/multiple_phone_datast.csv', index=False)
print('Data Saved')