from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/global/in-en/Computer-Systems/Store/ID-3'
uClient =  uReq(my_url)
page_html = uClient.read()
page_soup = soup(page_html, "html.parser")
#print(page_soup.p)
containers = page_soup.findAll("div", {"class":"item-info"})
#print(containers[1])
container  = containers[0]
title_container = container.findAll("span", {"class":"price-save-percent"})
print(title_container[0].text)
