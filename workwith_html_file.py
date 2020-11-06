from bs4 import BeautifulSoup

file = open('./Data/test_html_file.html').read()
# print(file)

soup = BeautifulSoup(file, 'lxml')
# print(soup)

# print(soup.find('table'))
print(soup.prettify())