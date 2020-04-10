from tkinter import *
import os
from PIL import ImageTk,Image
from Component import Component

class Titlebar(Component):
	def __init__(self,master):
		ROW = 0

		ICON_PATH = 'image/icon.jpg'
		ICON_HEIGHT = 32
		ICON_WIDTH = 30
		ICON_COLUMN = 0

		LABEL_HEIGHT = 1
		LABEL_WIDTH = 98
		LABEL_BG = '#66ffff'
		LABEL_COLUMN = 1

		QUITBUTTON_HEIGHT = 30
		QUITBUTTON_WIDTH = 30
		QUITBUTTON_PATH = 'image/quitbutton.png'
		QUITBUTTON_COLUMN = 3

		MINIMIZEBUTTON_HEIGHT = 30
		MINIMIZEBUTTON_WIDTH = 30
		MINIMIZEBUTTON_PATH = 'image/minimizebutton.jpg'
		MINIMIZEBUTTON_COLUMN = 2

		TITLEBAR_RELIEF = RAISED
		TITLEBAR_BG = "#66ffff"

		super(Titlebar, self).__init__(master,TITLEBAR_RELIEF,TITLEBAR_BG)
		self.master.overrideredirect(True)

		self.icon_img = ImageTk.PhotoImage( Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),ICON_PATH)))
		self.icon = Label(self,image=self.icon_img,height=ICON_HEIGHT,width=ICON_WIDTH)
		self.icon.grid(row=ROW,column=ICON_COLUMN)

		self.label1 = Label(self,text='Image Process App',height=LABEL_HEIGHT,width=LABEL_WIDTH,bg=LABEL_BG)
		self.label1.grid(row=ROW,column=LABEL_COLUMN)

		self.quitbutton_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),QUITBUTTON_PATH)))
		self.quitbutton = Button(self,image=self.quitbutton_img,command = self.master.quit,height=QUITBUTTON_HEIGHT,width=QUITBUTTON_WIDTH)
		self.quitbutton.grid(row=ROW,column=QUITBUTTON_COLUMN)

		self.minimizebutton_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),MINIMIZEBUTTON_PATH)))
		self.minimizebutton = Button(self,image=self.minimizebutton_img,command = self.Minimize,height=MINIMIZEBUTTON_HEIGHT,width=MINIMIZEBUTTON_WIDTH)
		self.minimizebutton.grid(row=ROW,column=MINIMIZEBUTTON_COLUMN)
		
		self.grid(row=0,column=0,columnspan=2)


		self.grid(row=0,column=0)
		self.bind("<Map>",self.Frame_mapped)

	def Frame_mapped(self,e):
		self.master.update_idletasks()
		self.master.overrideredirect(True)
		self.master.state('normal')

	def Minimize(self):
		self.master.update_idletasks()
		self.master.overrideredirect(False)
		self.master.state('iconic')
