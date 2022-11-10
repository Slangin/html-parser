from bs4 import BeautifulSoup
import sys


#Open local file
html_page = sys.argv[1]

clean_links = []
test = []

soup = BeautifulSoup(open(html_page),'html.parser')
images = soup.findAll('img')
links = soup.findAll('a')
link_1 = soup.findAll('link')
script = soup.findAll('script')

#Loop through alt image tags and santize paths
for image in images:
    image['src'] = image['src'].replace(' ', '-').replace('%20', '-').lower()
    
#Loop through link tags, ignore #, and sanitize paths
for link in links:
    if link['href'][0] != '#':
        link['href'] = link['href'].replace(' ', '-').replace('%20', '-').lower()
        
#Loop through script tags and sanitize path references       
for sc in script:
    sc['src'] = sc['src'].replace(' ', '-').replace('%20', '-').lower()
   
#Loop through link tags, ignore #, sanitize path references
for lk in link_1:
    if lk['href'][0] != '#':
        lk['href'] = lk['href'].replace(' ', '-').replace('%20', '-').lower()
        
#open or create a new file and update the path information
with open(sys.argv[2], 'w') as file:
    file.write((soup.prettify()))
