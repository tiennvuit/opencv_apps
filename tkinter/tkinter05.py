from tkinter import *

window = Tk()
window.title("Add button")
window.geometry("500x400")

lbl = Label(window, text="Hello", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)

btn = Button(window, text="Click me")
btn.grid(column=0, row=2)

window.mainloop()
