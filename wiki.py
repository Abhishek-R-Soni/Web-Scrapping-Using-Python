# getting titles, references data from wikipedia

import requests, bs4

res = requests.get('https://apps.supremecourt.az.gov/publicaccess/caselookup.aspx')
soup = bs4.BeautifulSoup(res.content, 'lxml')

# getting titles 
titles = soup.select('.mw-headline')
for title in titles:
    print(title.getText())

# getting references
references = soup.select('.reference-text')
for reference in references:
    print('* ', reference.getText())

