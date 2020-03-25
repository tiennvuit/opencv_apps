from tkinter import *

from tkinter import scrolledtext

window = Tk()
window.title("Add a ScrolledText widget (Tkinter textarea)")
window.geometry('350x200')

txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.grid(column=0, row=0)
