
from bs4 import BeautifulSoup
import requests
# Set url
url = "https://www.thedailystar.net/"

# Prepare response object to get the webpage
response = requests.get(url)

# Get all source code in text
data = response.text

# Pass the source code to beautiful soup to create BS object
soup = BeautifulSoup(data, 'html.parser')

# Extract all <a> tag from it
tags = soup.find_all('a')
# print(tags)

# Now extract url from it
for tag in tags:
    print(tag.get('href'))