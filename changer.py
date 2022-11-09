from bs4 import BeautifulSoup
import urllib.request
import urllib
import re
import sys


#Open local file
html_page = sys.argv[1]

clean_links = []
test = []

soup = BeautifulSoup(open(html_page),'html.parser')

for link in soup.findAll("a", href=True):
    cleaner = link['href']
    clean_links.append(cleaner)


for hl in clean_links:
    urllib.parse.unquote(hl)
    test.append(hl)



print(clean_links)
print(test)

    



