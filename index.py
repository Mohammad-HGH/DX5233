# Import Module
from bs4 import BeautifulSoup
import requests

# Website URL
URL = 'https://www.varzesh3.com/'

# Page content from Website URL
page = requests.get(URL).text



soup = BeautifulSoup(page, 'html.parser')
for s in soup.select('script'):
    s.extract()
# print(soup)
for s in soup.select('img'):
    s.extract()
with open('readme.html', 'w',encoding='utf-8') as f:
    f.write(str(soup))
