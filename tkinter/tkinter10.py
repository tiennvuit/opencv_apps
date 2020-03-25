from tkinter import *

window = Tk()
window.title("Get input using Entry class (Tkinter textbox")
window.geometry("600x400")

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

txt = Entry(window, width=10, state='disabled')
txt.grid(column=1, row=0)

def clicked():
    text = txt.get()
    lbl.configure(text=text)

btn = Button(window, text="Click me", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()
