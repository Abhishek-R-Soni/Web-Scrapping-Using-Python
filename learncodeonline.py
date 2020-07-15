# fatching site data
import requests
import bs4

res = requests.get('https://web.learncodeonline.in/')

# print(type(res)) # <class 'requests.models.Response'>
# print(res.text) # print html page content in text format

soup = bs4.BeautifulSoup(res.text, 'lxml') # convert text into tree format
h2 = soup.select('noscript') # pick "noscript" tag from code
print(h2[0]) # print 1st value from list
print(h2[0].getText()) # print only text value

tit = soup.select('title') # pick title
print(tit[0])

script = soup.select('script') # pick "script" tag from code
print(script[0])
