from tkinter import *

window = Tk()
window.title("Set window size")
window.geometry('1024x768')

lbl = Label(window, text="Hello", font=("Arial Bold", 10))
lbl.grid(column=200, row=200)

window.mainloop()
