from tkinter import *
import os
from PIL import ImageTk,Image
from Component import Component
from Titlebar import Titlebar
from Modebar import Modebar
from Image_executer import Image_executer 


class Application(object):
	HEIGHT = 600
	WIDTH = 800

	def __init__(self,master):
		self.master = master
		self.titlebar = Titlebar(self.master)
		self.modeoptionbar = Modebar(self.master)
		self.image_executer = Image_executer(self.master)

	def Run(self):
		window_height = Application.HEIGHT
		window_width = Application.WIDTH
		screen_width = self.master.winfo_screenwidth()
		screen_height = self.master.winfo_screenheight()
		x_cordinate = int((screen_width/2) - (window_width/2))
		y_cordinate = int((screen_height/2) - (window_height/2))
		self.master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
		self.master.mainloop()

	def Close(self):
		self.master.quit()


root = Tk()
a = Application(root)
a.Run()
