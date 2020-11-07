from bs4 import BeautifulSoup

file = open('./Data/three_sisters.html.html').read()
# print(file)

soup = BeautifulSoup(file, 'lxml')
# print(soup)

# print(soup.find('table'))
# print(soup.prettify())
# print(soup)

# Title
# print(soup.title.prettify())

# Paragraph (Default First p)
# print(soup.p.prettify())

# All paragraph
body = soup.body
for i in body.contents:
    print(i if i is not None else '')