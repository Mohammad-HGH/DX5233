from lxml.etree import tostring
import lxml.html
import requests
from adremover import AdRemover

url = 'https://soft98.ir'  # replace it with a url you want to apply the rules to  
rule_urls = ['ruadlist+easylist.txt', '1.txt']

rule_files = [url.rpartition('/')[-1] for url in rule_urls]





remover = AdRemover(*rule_files)

html = requests.get(url).text
document = lxml.html.document_fromstring(html)
remover.remove_ads(document)
clean_html = tostring(document).decode("utf-8")

with open('readme.html', 'w') as f:
    f.write(clean_html)