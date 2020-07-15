# getting all links from wiki ML page and convert into json file then store it.

# import requests, bs4

# res = requests.get('https://apps.supremecourt.az.gov/publicaccess/caselookup.aspx')
# soup = bs4.BeautifulSoup(res.text, 'lxml')

# links = soup.find_all('a',href=True)
# import webbrowser

# for link in links:
#     print(link['href'])
#     webbrowser.open(link['href'])



# ls = list()

# for link in links:
#     ls.append({'title':'Machine Learning',
#                 'link':link['href']
#              })
# print(ls)

# with open('demo.txt', 'a') as f:
#     f.write(str(ls))



ar = [1,2,3,4,5]

for i in range(2):
    temp = ar.pop(0)
    print(temp)
    ar.append(temp)
    print(ar)