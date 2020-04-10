from tkinter import * 
import os.path as osp
from PIL import ImageTk,Image
from Component import Component
import cv2 as cv
from tkinter import filedialog
import os.path


class Image_executer(Component):
	IMAGE_PATH = 'image/icon-image-512.png'
	PREVIOUS_PATH = 'image/previos_arrow.png'
	NEXT_PATH = 'image/next_arrow.jpg'
	PADY = 15
	BUTTON_PADY = 165
	HEIGHT = 600
	WIDTH = 200
	IMAGE_SIZE = (460,380)
	MAX_ELEMENT = 40

	def __init__(self,master):
		super(Image_executer, self).__init__(master,height=Image_executer.HEIGHT,width=Image_executer.WIDTH,bg ='#fcba03')
		self.firstbutton_img = ImageTk.PhotoImage(Image.open(osp.join(osp.dirname(osp.abspath(__file__)),
			Image_executer.PREVIOUS_PATH)))
		self.firstbutton = Button(self,image=self.firstbutton_img,state='disabled')
		self.firstbutton.grid(row=0,column=0,pady=Image_executer.BUTTON_PADY,sticky=N)
		self.firstbutton.bind('<Button-1>',self.Return_back)

		self.original = Image.open(Image_executer.IMAGE_PATH)
		self.image = ImageTk.PhotoImage(self.original.resize(Image_executer.IMAGE_SIZE,Image.ANTIALIAS))
		self.display = Canvas(self, bd=0, highlightthickness=0,width=Image_executer.IMAGE_SIZE[0])
		self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")
		self.display.grid(row=0,column=1,pady=(Image_executer.PADY,0), sticky=N+S)

		self.secondbutton_img = ImageTk.PhotoImage(Image.open(osp.join(osp.dirname(osp.abspath(__file__)),
			Image_executer.NEXT_PATH)))
		self.secondbutton = Button(self,image=self.secondbutton_img,state='disabled')
		self.secondbutton.grid(row=0,column = 2,pady=Image_executer.BUTTON_PADY,sticky=N)
		self.secondbutton.bind('<Button-1>',self.Come_next)

		self.thirdbutton = Button(self,text='Load an image',width=60)
		self.thirdbutton.grid(row=1,column = 0,columnspan=3,sticky=N)
		self.thirdbutton.bind('<Button-1>',self.Load)

		self.grid(row=2,column=1,columnspan=2,sticky=W)
		self.it = 0
		self.pq = []

	def change_image(self,image):
		image = Image.fromarray(image)
		self.image = ImageTk.PhotoImage(image.resize(Image_executer.IMAGE_SIZE,Image.ANTIALIAS))
		self.display.delete("IMG")
		self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")

	def Load(self,event):
		self.path = filedialog.askopenfilename(initialdir = os.path.dirname(os.path.abspath(__file__)),title = "Select file",
			                                    filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
		if len(self.path) == 0:
			return
		img = cv.cvtColor(cv.imread(self.path),cv.COLOR_BGR2RGB)
		self.change_image(img)
		if len(self.pq)>0:
			del self.pq[self.it+1:len(self.pq)]
		self.pq.append(img)
		if len(self.pq) > Image_executer.MAX_ELEMENT:
			del self.pq[0]
		self.it = len(self.pq)-1
		self.Reset_state()

	def Transform(self,img):
		self.change_image(img)
		self.Reset_state()

	def Return_back(self,event):
		if self.it == 0:
			self.it = len(self.pq)-1
		else:
			self.it = self.it - 1
		self.change_image(self.pq[self.it])

	def Come_next(self,event):
		if self.it == len(self.pq)-1:
			self.it = 0
		else:
			self.it = self.it + 1
		self.change_image(self.pq[self.it])

	def Reset_state(self):
		if len(self.pq) >= 2:
			self.firstbutton.configure(state='normal')
			self.secondbutton.configure(state='normal')
		else:
			self.firstbutton.configure(state='disabled')
			self.secondbutton.configure(state='disabled')


