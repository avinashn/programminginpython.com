__author__ = 'Avinash'

from tkinter import *
root = Tk()

root.geometry('200x200+100+200')

Label(root, text="Label 1 : x=0, y=0", bg="#FFFF00", fg="black").place(x=0, y=0)
Label(root, text="Label 2 : x=50, y=40", bg="#3300CC", fg="white").place(x=50, y=40)
Label(root, text="Label 3 : x=75, y=80", bg="#FF0099", fg="black").place(x=75, y=80)
Label(root, text="Label 4 : x=25, y=100", bg="#00FFFF", fg="white").place(x=25, y=100)

mainloop()
