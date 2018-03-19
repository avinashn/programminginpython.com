__author__ = 'Avinash'

import tkinter as tk
import socket
from functools import partial


# the main conversion
def call_convert(rlabel1, inputn):
    try:
        ip = (socket.gethostbyname(inputn.get()))
        rlabel1.config(text="The IP address of domain " + inputn.get() + " is " + ip)
    except Exception:
        rlabel1.config(text="Please enter a valid url and in the form 'www.example.com'")
    return


# app window configuration and UI
root = tk.Tk()

# Gets the requested values of the height and width.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

root.geometry("600x200+{}+{}".format(positionRight, positionDown))
root.title('Domain to IP Converter')
root.configure(background='#009688')
root.resizable(width=False, height=False)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(2, weight=1)

contents = tk.Frame(root)
contents.grid(row=1, column=1)

domainInput = tk.StringVar()

# label and entry field
input_label = tk.Label(root, text="Enter domain", background='#009688', foreground="#FFFFFF")
input_entry = tk.Entry(root, textvariable=domainInput)
input_label.grid(row=1)
input_entry.grid(row=1, column=1)

# result label's for showing the IP of a domain
result_label1 = tk.Label(root, background='#009688', foreground="#FFFFFF")
result_label1.grid(row=3, columnspan=4)

# button click
call_convert = partial(call_convert, result_label1, domainInput)
result_button = tk.Button(root, text="Convert", command=call_convert, background='#FFFFFF', foreground="#009688")
result_button.grid(row=2, columnspan=4)

root.mainloop()
