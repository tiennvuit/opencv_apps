from tkinter import *

class Component(Frame):
	def __init__(self,the_window,relief='raised',bg="WHITE",width=111):
		super().__init__()
		self["relief"] = relief
		self["bg"] = bg
		self["width"] = width

	def Disable(self):
		for child in self.winfo_children():
			child.configure(state='disable')
		self.lower()

	def Enable(self):
		for child in self.winfo_children():
			child.configure(state='normal')
		self.lift()
