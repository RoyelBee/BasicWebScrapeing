from bs4 import BeautifulSoup

file = open('./Data/three_sisters.html.html').read()
# print(file)

soup = BeautifulSoup(file, 'lxml')
# print(soup)
# P tag in under body tag
parent = soup.p.parent
# print(parent.name)

a = soup.a
# print(a.parent.name)

# HTML type
html = soup.html
# print(type(html.parent))

# Access all parent tag
links = soup.a

# for link in links.parents:
#     print(link.name)

