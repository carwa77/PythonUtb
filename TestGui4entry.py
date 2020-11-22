#Test av dialogruta
from tkinter import *

root = Tk()
e = Entry(root,width=50)
e.pack()
e.insert(0,"Skriv ditt namn")

def myclick():
    hello = "Hej " +e.get()
    mylabel = Label(root, text=hello)
    mylabel.pack()
    
myButton = Button(root, text = "Enter your name", command=myclick)
myButton.pack()    

root.mainloop()
