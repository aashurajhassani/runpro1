from tkinter import *
import tkinter as tk
WebScrapper = tk.Tk()
w = Canvas(WebScrapper, width=500, height=250)
w.pack()

label1 = tk.Label(WebScrapper, text='Type the Web Address:')
label1.config(font=('helvetica', 10))
w.create_window(150, 125, window=label1)

webaddress = tk.Entry (WebScrapper) 
w.create_window(300, 125, window=webaddress)
  
label2 = tk.Label(WebScrapper, text='Type the word to be counted:')
label2.config(font=('helvetica', 10))
w.create_window(150, 150, window=label2)

word = tk.Entry (WebScrapper) 
w.create_window(300, 150, window=word)

def getInfo ():
    address = webaddress.get()      #use this variable for getting the webaddress
    findword = word.get()               #use this variable for getting the word
    label3 = tk.Label(WebScrapper, text= "output")     #in place of output write wordcount after getting it
    w.create_window(250, 250, window=label3)

button1 = tk.Button(text='Enter', command=getInfo)
w.create_window(250, 175, window=button1)

WebScrapper.mainloop()
