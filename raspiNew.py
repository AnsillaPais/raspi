import serial
import pyttsx3
import os
import time
import sys

if sys.version_info[0] == 2:
	import Tkinter
	tkinter = Tkinter
else:
 	import tkinter
from PIL import Image, ImageTK

dispOpenIndicator = 0

def speak():
	engine = pyttsx3.init()
	engine.say("Hello Welcome to SJEC!!")
	engine.runAndWait()

def display():
	im = Image.open(r"/home/raspi/Downloads/tree5.jpg")
	im.show()

if __name__ == '__main__':
	ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
	ser.flush()
	while True:
		if ser.in_waiting > 0:
			data = ser.readline().decode('utf-8').rstrip()
			print(data)
			if data == "1":
				print("Success")
				speak()
				display()
				while True:
					data  = ser.readline().decode('utf-8').rstrip()
					if data == "0":
						break