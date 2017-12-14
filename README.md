# Raspberry-Spy

## Introduction

design and implement a Raspberry Pi 3 based low-cost smart surveillance monitoring system. 
With RPi3 on board Wi-Fi, Pi Camera and Motion Eye OS you will be able to capture High Definition video and live stream video can be accessed/viewed using a web browser from anywhere by just entering the static RPi IP address.
The system can automatically initiate video recording, image capturing or send notifications if any kind of motion is detected.

our team has used Raspbian os and open cv(because open cv provides standaed things such as image capture,image manipulation and all these specifications meet our requirements)

## Operation

Capture image
Get distance information (clear vision of a photo)
Send collected data to the server (sending the motion video or picture to a server)
Process data
Get response 

## Mainmodule

 Camera interfacing
 
 image capturing
 
 connecting with hardware
 
 Motion detection

## system Analysis and Design

model-Respberry pi3
PIR sensor
Sensor output volt =5v
respberry configuration

## Pseudo code

DISPLAYING THE IMAGE

from openCV import Image, Display
from time import sleep 
myDisplay = Display() 
raspberryImage = Image("raspberries.jpg") 
raspberryImage.save(myDisplay) 
while not myDisplay.isDone(): 
sleep(0.1) 

Modifying and Saving an image

from openCV import Image, DrawingLayer, Color 
from time import sleep 
raspberryImage = Image("raspberries.jpg") 
myDrawingLayer = DrawingLayer((raspberryImage.width, raspberryImage.height)) 
myDrawingLayer.rectangle((50,20), (250, 60), filled=True) 
myDrawingLayer.setFontSize(45) 
myDrawingLayer.text("Raspberries!", (50, 20), color=Color.WHITE) 
raspberryImage.addDrawingLayer(myDrawingLayer) 
raspberryImage.applyLayers() 
raspberryImage.save("raspberries-titled.jpg") 

Face Detection

from openCV import Camera, Display 
from time import sleep 
myCamera = Camera(prop_set={'width':320, 'height': 240}) 
myDisplay = Display(resolution=(320, 240)) 
while not myDisplay.isDone(): 
frame = myCamera.getImage() 
faces = frame.findHaarFeatures('face') 
if faces: 
for face in faces: 
print "Face at: " + str(face.coordinates()) 
else: 
print "No faces detected." 
           frame.save(myDisplay) 
 sleep(.1)  

Twitter interfacing

Sudo pip-install twython

We have used twitter because we easily get the api of twitter and its keys.

ENJOY !
