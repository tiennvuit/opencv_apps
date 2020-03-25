from tkinter import *
import os
from PIL import ImageTk,Image
from Component import Component

class Application(object):
	def __init__(self,master):
		self.master = master
		self.Create_title_bar()
		self.Create_modeoption_bar()

		#self.label = Button(self.master,text="Hello world")
		#self.label.grid(row=1,column=0)


	def Run(self):
		window_height = 600
		window_width = 800
		screen_width = self.master.winfo_screenwidth()
		screen_height = self.master.winfo_screenheight()
		x_cordinate = int((screen_width/2) - (window_width/2))
		y_cordinate = int((screen_height/2) - (window_height/2))
		self.master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
		self.master.mainloop()

	def Close(self):
		self.master.quit()

	def Frame_mapped(self,e):
		print(self,e)
		self.master.update_idletasks()
		self.master.overrideredirect(True)
		self.master.state('normal')

	def Minimize(self):
		self.master.update_idletasks()
		self.master.overrideredirect(False)
		self.master.state('iconic')

	def Create_title_bar(self):
		self.master.overrideredirect(True)

		self.titlebar = Component(self.master,relief=RAISED,bg='#66ffff')

		self.icon_img = ImageTk.PhotoImage( Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'image','icon.jpg')))
		self.icon = Label(self.titlebar,image=self.icon_img,height=32,width=30)
		self.icon.grid(row=0,column=0)

		self.label1 = Label(self.titlebar,text='Image Process App',height=1,width=98,bg='#66ffff')
		self.label1.grid(row=0,column=1)

		self.quitbutton_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'image','quitbutton.PNG')))
		self.quitbutton = Button(self.titlebar,image=self.quitbutton_img,command = self.Close,height=30,width=30)
		self.quitbutton.grid(row=0,column=3)

		self.minimizebutton_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'image','minimizebutton.jpg')))
		self.minimizebutton = Button(self.titlebar,image=self.minimizebutton_img,command = self.Minimize,height=30,width=30)
		self.minimizebutton.grid(row=0,column=2)


		self.titlebar.grid(row=0,column=0)
		self.titlebar.bind("<Map>",self.Frame_mapped)

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


	def Create_modeoption_bar(self):
		self.modeoptionbar = Component(self.master,width=90)
		self.firstbutton = Button(self.modeoptionbar,text='Image',width=55)
		self.firstbutton.grid(row=0,column=0)
		self.firstbutton.bind('<Button-1>',self.Reset_mode)
		self.secondbutton = Button(self.modeoptionbar,text='Video',width=55)
		self.secondbutton.grid(row=0,column=1)
		self.secondbutton.bind('<Button-1>',self.Reset_mode)
		self.thirdbutton = Button(self.modeoptionbar,text='Stream',width=112)
		self.thirdbutton.grid(row=1,column=0,columnspan=2)
		self.thirdbutton.bind('<Button-1>',self.Reset_mode)
		self.modeoptionbar.grid(row=1,column=0)


root = Tk()
a = Application(root)
print(type(a))
a.Run()
