__author__ = 'Avinash'

from tkinter import *

root = Tk()
root.geometry('400x400+100+200')

# fill option
label1 = Label(root, text="Label 1", bg="#E74C3C", fg="white").pack(fill=X, padx=10)
label2 = Label(root, text="Label 2", bg="#2ECC71", fg="black").pack(fill=X, padx=10)
label3 = Label(root, text="Label 3", bg="#F1C40F", fg="white").pack(fill=X, padx=10)

# side option
label4 = Label(root, text="Label 1", bg="#34495E", fg="white").pack(fill=X, padx=10, pady=10, side=LEFT)
label5 = Label(root, text="Label 2", bg="#5DADE2", fg="black").pack(fill=X, padx=10, side=LEFT)
label6 = Label(root, text="Label 3", bg="#A569BD", fg="white").pack(fill=X, padx=10, side=LEFT)

# expand option
listbox = Listbox(root)
listbox.pack(fill=BOTH, expand=1)

for i in range(20):
    listbox.insert(END, str(i))

mainloop()
