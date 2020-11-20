
import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlrd

# # ----------------------------------------
# # -------- Part 01 -----------------------
# # ----------------------------------------

main_url = 'https://codingbat.com/java'
base_url = 'https://codingbat.com'
page = requests.get(main_url)
soup = BeautifulSoup(page.content, 'lxml')
# print(soup)

all_div = soup.find_all('div', class_='summ')

# # Get all sections links --------------------
# section_links  = []
#
# for div in all_div:
#     # print(div.a['href']) # Gives all alternative links
#     link = base_url + div.a['href']
#     section_links.append(link)

# # Another short way to get all sections links ------
section_links = [base_url + div.a['href'] for div in all_div]

# # ---------------------------------------------------------
# # ------------- Part 02 -----------------------------------
# # ---------------------------------------------------------

# # Now find each sections individual links
q     = []
title = []
exp   = []

for link in section_links:
    inner_page = requests.get(link)
    inner_soup = BeautifulSoup(inner_page.content, 'lxml')

    div = inner_soup.find('div', class_='tabc')

    ## Now find all tdd in the table
    # for td in div.table.find_all('td'):
    #     print(td)
    #     get all questions link
    #     print(base_url+ td.a['href'])

    # Short way to get all questions link
    questions_link = [base_url + td.a['href'] for td in div.table.find_all('td')]

    # # -------------------------------------------------------------------------
    # # -------- Part 03 Extract final questions --------------------------------
    # # -------------------------------------------------------------------------

    for question in questions_link:
        q_link = requests.get(question)
        q_soup = BeautifulSoup(q_link.content, 'lxml')

        indent_div = q_soup.find('div', class_='indent')
        problem_statement = indent_div.table.div.text
        problem_sibling   = indent_div.table.div.next_siblings

        # for sibling in problem_sibling:
        #     if sibling.string is not None:
        #         # print(sibling)

        # Short way
        q_examples = [sibling for sibling in problem_sibling if sibling.string is not None]

        # Show all questions link , Title and its example -------------------------------
        # print('\n\n')
        print(question)
        # print(problem_statement)
        # for examples in q_examples:
        #     print(examples)

        q.append(question)
        title.append(problem_statement)
        exp.append(q_examples)


# # -----------------------------------------------------
# # ----------- Part 04 Save result data ----------------
# # -----------------------------------------------------

df = pd.DataFrame()
df['Link'] = q
df['Title'] = title
df['Examples'] = exp

df.to_excel('Data/All_java_questions.xlsx', index=False)
print('Data Saved')