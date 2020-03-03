from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/global/in-en/Computer-Systems/Store/ID-3'
uClient =  uReq(my_url)
page_html = uClient.read()
page_soup = soup(page_html, "html.parser")
#print(page_soup.p)
containers = page_soup.findAll("div", {"class":"item-branding"})

brand = input("Enter the brand name: ").lower()
count = 0
for i in range(0, len(containers)):
    if brand == (containers[i].img['alt']).lower():
        count += 1
print(count) 
