from tkinter import *
import tkinter as tk

WebScrapper = tk.Tk()
w = Canvas(WebScrapper, width=500, height=250)
w.pack()

label1 = tk.Label(WebScrapper, text='Type the Web Address:')
label1.config(font=('helvetica', 10))
w.create_window(150, 125, window=label1)

webaddress = tk.Entry(WebScrapper)
w.create_window(300, 125, window=webaddress)

label2 = tk.Label(WebScrapper, text='Type the word to be counted:')
label2.config(font=('helvetica', 10))
w.create_window(150, 150, window=label2)

word = tk.Entry(WebScrapper)
w.create_window(300, 150, window=word)


def getInfo():
    address = webaddress.get()  # use this variable for getting the webaddress
    findword = word.get()  # use this variable for getting the word
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup

    my_url = address
    uClient = uReq(my_url)
    page_html = uClient.read()
    page_soup = soup(page_html, "html.parser")
    # code for parsing html code
    containers = page_soup.findAll("div", {"class": "mw-body-content"})
    wordlist = []

    '''creating two lists: one which containers
        the code of all div tags and the other
        one will store the text of the page'''

    for each_text in containers:
        content = each_text.text  # accessing the text in the tags
        words = content.lower().split()  # converting to lowercase and splitting
        # paragraphs into words
        for each_word in words:
            wordlist.append(each_word)

    input = findword.lower()

    symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
    symbols = symbols + "'"

    # defining a list of symbols which must be
    # eliminated to get the meaningful word
    count = 0
    for i in range(0, len(wordlist)):
        current = wordlist[i]
        for p in range(0, len(symbols)):
            current = current.replace(symbols[p], '')
        if input == current:
            count += 1

    label3 = tk.Label(WebScrapper, text=count)  # in place of output write wordcount after getting it
    w.create_window(250, 250, window=label3)


button1 = tk.Button(text='Enter', command=getInfo)
w.create_window(250, 175, window=button1)

WebScrapper.mainloop()
