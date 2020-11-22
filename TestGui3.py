from tkinter import *

root = Tk()

mylabel = Label(root, text="Hello")
mylabel1 = Label(root, text="Jag heter Calle")

mylabel.grid(row=0,column=0)
mylabel1.grid(row=1,column=0)



root.mainloop()