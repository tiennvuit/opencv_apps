from tkinter import *

window = Tk()
window.title("Change button foreground and background colors")
window.geometry("500x400")

lbl = Label(window, text="Hello", font=("Arial Itali", 30))
lbl.grid(column=0, row=0)

btn = Button(window, text="Click me", bg="orange", fg="blue")
btn.grid(column=1, row =0)

window.mainloop()
