from tkinter import *
import os
from PIL import ImageTk,Image
from Component import Component

class Modebar(Component):
	def __init__(self,master):
		MODEBAR_WIDTH = 90
		ROW1 = 0
		ROW2 = 1
		FIRSTBUTTON_WIDTH = 55
		FIRSTBUTTON_COLUMN = 0
		SECONDBUTTON_WIDTH = 55
		SECONDBUTTON_COLUMN = 1
		THIRDBUTTON_WIDTH = 112
		THIRDBUTTON_COLUMN = 0

		super(Modebar, self).__init__(master,width=MODEBAR_WIDTH)
		self.firstbutton = Button(self,text='Image',width=FIRSTBUTTON_WIDTH)
		self.firstbutton.grid(row=ROW1,column=FIRSTBUTTON_COLUMN)
		self.firstbutton.bind('<Button-1>',self.Reset_mode)
		self.secondbutton = Button(self,text='Video',width=SECONDBUTTON_WIDTH)
		self.secondbutton.grid(row=ROW1,column=SECONDBUTTON_COLUMN)
		self.secondbutton.bind('<Button-1>',self.Reset_mode)
		self.thirdbutton = Button(self,text='Stream',width=THIRDBUTTON_WIDTH)
		self.thirdbutton.grid(row=ROW2,column=THIRDBUTTON_COLUMN,columnspan=2)
		self.thirdbutton.bind('<Button-1>',self.Reset_mode)
		self.grid(row=1,column=0)

	def Reset_mode(self,event):
		str = event.widget.cget("text")
		if str=="Image":
			self.firstbutton.configure(text="Video")
			self.secondbutton.configure(text="Stream")
			self.thirdbutton.configure(text="Image")
			return
		if str=="Video":
			self.firstbutton.configure(text="Image")
			self.secondbutton.configure(text="Stream")
			self.thirdbutton.configure(text="Video")
			return
		if str=="Stream":
			self.firstbutton.configure(text="Image")
			self.secondbutton.configure(text="Video")
			self.thirdbutton.configure(text="Stream")
			return
