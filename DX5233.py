from lxml.etree import tostring
import lxml.html
import requests
from adremover import AdRemover
from bs4 import BeautifulSoup

url = 'https://www.zoomit.ir'  # replace it with a url you want to apply the rules to  
rule_urls = ['ruadlist+easylist.txt', '1.txt']

rule_files = [url.rpartition('/')[-1] for url in rule_urls]





remover = AdRemover(*rule_files)

html = requests.get(url).text
document = lxml.html.document_fromstring(html)
remover.remove_ads(document)
clean_html = tostring(document).decode("utf-8")
soup=BeautifulSoup(clean_html)
# print(BeautifulSoup(clean_html))
with open('readme.html', 'w',encoding='utf-8') as f:
    f.write(str(soup))