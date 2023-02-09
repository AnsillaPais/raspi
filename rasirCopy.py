import serial
import pyttsx3
import os
#from PIL import Image
import time

import sys
if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
    import Tkinter
    tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
else:
    import tkinter
from PIL import Image, ImageTk

#constants
dispOpenIndicator = 0

def speak():
	engine = pyttsx3.init()
	engine.say("Hello welcome to SJEC")
	engine.runAndWait()

def showPIL(pilImage):
	root = tkinter.Tk()
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.overrideredirect(1)
	root.geometry("%dx%d+0+0" % (w, h))
	root.focus_set()
	root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
	canvas = tkinter.Canvas(root,width=w,height=h)
	canvas.pack()
	canvas.configure(background='black')
	imgWidth, imgHeight = pilImage.size
	if imgWidth > w or imgHeight > h:
		ratio = min(w/imgWidth, h/imgHeight)
		imgWidth = int(imgWidth*ratio)
		imgHeight = int(imgHeight*ratio)
		pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
	image = ImageTk.PhotoImage(pilImage)
	imagesprite = canvas.create_image(w/2,h/2,image=image)
	canvas.bind("<Return>", lambda e: root.destroy())
	root.mainloop()


def display():
	im = Image.open(r"/home/raspi/Downloads/tree5.jpg")
	showPIL(im)
	dispOpenIndicator = 1


if __name__=='__main__':
	ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
	ser.flush()
	while  True:
		if ser.in_waiting > 0:
			print(data)
			data = ser.readline().decode('utf-8').rstrip()
			print(data)
			#print(type(data))
			if data == "1":
				print("Success!")
				speak()
				print(data)
				if dispOpenIndicator == 0:
					display()