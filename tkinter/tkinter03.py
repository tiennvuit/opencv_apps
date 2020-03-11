from tkinter import *

window = Tk()
window.title("Set fontsize for text")

lbl = Label(window, text="Hello", font=("Arial Bold", 50))

lbl.grid(column=0, row=0)

window.mainloop()
