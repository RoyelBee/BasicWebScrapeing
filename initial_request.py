import requests as re
from bs4 import BeautifulSoup as bs
url = "https://www.monster.com/jobs/search/?q=Developer&where=London"
page = re.get(url)
soup = bs(page.content, 'html.parser')
