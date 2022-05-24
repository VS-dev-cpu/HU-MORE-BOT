# Konnichiwa!

# Importing the libs

from datetime import datetime
import calendar
import time

import os

from gpiozero import Button

import cv2
import numpy as np

import bt

# Setup for like... everything... I guess...
def unix():
	d = datetime.utcnow()
	return calendar.timegm(d.utctimetuple())

def send(data):
    os.system("echo '" + str(data) + "\\n' >> /dev/ttyS0")

#button = Button(26)
sensor = Button(19)

W = 320
H = 240

IMAGE_FLIP_VERTICALLY = False
IMAGE_FLIP_HORIZONTALLY = False
IMAGE_RESIZE = True

cap = cv2.VideoCapture(-1)

if (IMAGE_RESIZE):
    cap.set(3, int(W))
    cap.set(4, int(H))

#RED
low_acorn = np.array([161, 155, 84])
high_acorn = np.array([179, 255, 255])

W = cap.get(3)
H = cap.get(4)

size = 0
gap = 2.5
minSize = 150

debugging = False

bt = bt.BT()

### SERVER ONLY CODE ###
#while (1):
#	if not button.is_pressed:
#		break
#bt.start()

bt.sync()

send(10)
time.sleep(3)

start = unix()
duration = 60

#Limit Speed, To Avoid Message-Overflow (Between the RPi and Arduino) [Default: 0.05]
speedLimit = 0.05

# Main Loop

while True:
	# Read image from the camera
	ret, frame = cap.read()
    
	if not ret:
		print("ERROR: CAN NOT READ IMAGE FROM THE CAMERA")
		exit()
		
	# Exit in case of overtime
	if (unix() - start > duration):
		break;
		
	# Go around an object, if you see it
	if not sensor.is_pressed:
		send(30)
		time.sleep(5)
		
	# Flip the image
	if (IMAGE_FLIP_VERTICALLY):
		frame = cv2.flip(frame, 0)
	if (IMAGE_FLIP_HORIZONTALLY):
		frame = cv2.flip(frame, 1)
        
	# OpenCV Stuff
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv_frame, low, high)
	contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
   
	# Getting The Acorn's size
	size = 0
	for cnt in contours:
		(x, y, w, h) = cv2.boundingRect(cnt)
       
		size = int((w + h) / 2)
		break
    
	# The EXIT stuff is happening here
	key = cv2.waitKey(1)
	if (size > minSize or key == 27):
		break
	else:
		send(3)
	time.sleep(speedLimit)
    
# And The Final Dance
send(0)
send(20)

# After that, please destroy the windows and release the cap, because I won't need them anymore...
# And also quit from the program, because it uses quite a lot memory...
cap.release()
cv2.destroyAllWindows()
# Oyasumi!
