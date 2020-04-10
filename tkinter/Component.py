from tkinter import *

class Component(Frame):
	def __init__(self,the_window,relief='raised',bg='SystemButtonFace',width=0,height=0):
		super().__init__()
		self["relief"] = relief
		self["bg"] = bg
		self["width"] = width
		self["height"] = height
		self["bg"] = bg

	def Disable(self):
		for child in self.winfo_children():
			child.configure(state='disable')
		self.lower()

	def Enable(self):
		for child in self.winfo_children():
			child.configure(state='normal')
		self.lift()
