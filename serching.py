

from bs4 import BeautifulSoup

file = open('./Data/three_sisters.html.html').read()
# print(file)

soup = BeautifulSoup(file, 'lxml')

a = soup.find_all('a')
# print(a)

# # Limit peramiter ( Returns number of records)
# a = soup.find_all('a', limit=2)
# print(a)

# Find by class name
# cname = {'class': 'sister'}
# c = soup.find_all(attrs=cname)
# print(c)

# # Another way
# cc = soup.find_all(class_='sister')
# print(cc)