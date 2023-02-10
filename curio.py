import serial
import os
import sys
import time
import pyttsx3

from PIL import Image

def speak():
    engine=pyttsx3.init()
    engine.say("Hi,I am curio  welcome to SJEC How can i help you")
    engine.runAndWait()
    
def display():
    im=Image.open(r"/home/raspi/Downloads/tree5.jpg")
    im.show()
    
if __name__ == '__main__':
    ser=serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()
    
    previousData=0
    
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            print(data)
            if data == "1":
                if previousData == 0:
                    previousData=1
                    print("Success")
                    speak()
                    display()
            else:
                previousData=0
    
