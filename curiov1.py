import serial
import os
import sys
import time
import pyttsx3
from PIL import Image



def speak():
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('rate',150)
    engine.say("Hi")
    engine.runAndWait()
    engine.say("I am curio")
    engine.runAndWait()
    engine.say("Welcome to S J E C")
    engine.runAndWait()
    engine.say("How can I help you??")
    engine.runAndWait()
    
    
def display():
    im=Image.open(r"/home/raspi/Downloads/sjec.jpg")
    im.show()

    
if __name__ == '__main__':
    ser=serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    
    previousData=0
    display()
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            print(data)
            if data == "1":
                if previousData == 0:
                    previousData=1
                    print("Success")
                    speak()
            else:
                previousData=0
