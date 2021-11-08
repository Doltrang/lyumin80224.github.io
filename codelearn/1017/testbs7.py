from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/List_of_Nobel_laureates'
response = requests.get(url)
soup = BeautifulSoup(response.content,'lxml')

trs=soup.select('table')[0].select('tr')
print(trs[0].select('th')[3].select('a')[0].text.replace('or',' or'))