import pandas as pd
import requests as re
from bs4 import BeautifulSoup as bs
url = "https://www.monster.com/jobs/search/?q=Developer&where=London"
page = re.get(url)
soup = bs(page.content, 'html.parser')
results = soup.find(id="ResultsContainer")
# print(results.prettify())


# Find element by class
job_elements = results.find_all('section', class_='card-content')

t = []
c = []
l = []
# Sepaerate every job sections with  new lines and fetched actual data
for job in job_elements:
    title = job.find('h2', class_='title')
    company = job.find('div', class_='company')
    location = job.find('div', class_='location')
    if None in (title, company, location):
        continue

    # print(title.text.strip())
    # print(company.text.strip())
    # print(location.text.strip())
    # print()

    # # ------ Insert all related data in a list
    t.append(title.text.strip())
    c.append(company.text.strip())
    l.append(location.text.strip())


df = pd.DataFrame()
df['Job Title'] = t
df['Company'] = c
df['Location'] = l

# print(df.head())
df.to_csv('job_data.csv')
print('Data Saved')