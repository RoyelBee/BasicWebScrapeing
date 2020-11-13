from bs4 import BeautifulSoup
import requests
import pandas as pd


link = requests.get('https://www.mobilemaya.com/brand/samsung').text
soup = BeautifulSoup(link, 'html.parser')


# all_div = soup.find_all('div', attrs={'id':'name'})

## All Phone name at a glance
# for div in all_div:
#     print(div.a.text)


# # ------------------------------------------------------------------------------
# At a time phone name and their price ( All data are come from in a single page )
### ------------------------------------------------------------------------------

result = soup.find_all('div', attrs={'class': 'single'})
# print(result)
phone = []
price = []

for r in result:
    phone.append(r.find(id='name').text)
    price.append(r.find(id="price").text)

# print(price)
# print(phone)

df = pd.DataFrame()

df['Phone Name'] = phone
df['Price'] = price

# print(df.head())
df.to_csv('Data/phone_datast.csv', index=False)
print('Data Saved')