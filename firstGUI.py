__author__ = 'Avinash'

from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack(side=TOP)

middleFrame = Frame(root)
middleFrame.pack(side=RIGHT)

bottomFrame = Frame(root, bg="green")
bottomFrame.pack(side=BOTTOM)

topFrame_Label = Label(topFrame, text="Welcome to Python GUI(Top Frame)")
topFrame_Label.pack()

middleFrame_Label = Label(middleFrame, text="Welcome to Python GUI(Middle Frame)")
middleFrame_Label.pack()

bottomFrame_Label = Label(bottomFrame, text="Welcome to Python GUI(Bottom Frame)")
bottomFrame_Label.pack()
theButton = Button(bottomFrame, text="Button", fg="red", bg="black")
theButton.pack()
root.minsize(400, 400)
root.mainloop()
