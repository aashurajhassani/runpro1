from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = input("type wiki webpage here: ")
uClient =  uReq(my_url)
page_html = uClient.read()
page_soup = soup(page_html, "html.parser")
#code for parsing html code
containers = page_soup.findAll("div", {"class":"mw-body-content"})
wordlist = []

'''creating two lists: one which containers
    the code of all div tags and the other
    one will store the text of the page'''

for each_text in containers:
    content = each_text.text #accessing the text in the tags
    words = content.lower().split() #converting to lowercase and splitting
                                    #paragraphs into words
    for each_word in words:
        wordlist.append(each_word)

input = input("enter the word here: ").lower()

symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
symbols = symbols + "'"

# defining a list of symbols which must be
#eliminated to get the meaningful word
count = 0
for i in range(0, len(wordlist)):
    current = wordlist[i]
    for p in range(0, len(symbols)):
        current = current.replace(symbols[p], '')
    if input == current:
        count += 1

print(count)
