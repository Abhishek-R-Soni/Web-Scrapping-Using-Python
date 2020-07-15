# getting titles, references data from wikipedia

import requests, bs4

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
soup = bs4.BeautifulSoup(res.content, 'lxml')

# # getting titles 
# title = soup.select('title')
# print('Title : ', title[0].getText())

# # getting ML content
# contents = soup.select('.toctext')
# print('\nContent : ', end="")
# for content in contents:
#     print(content.getText())

# # getting links
links = soup.find_all('a', href = True)
for link in links:
    print('* ', link['href'])

