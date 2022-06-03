# The Code For The Pigs

from datetime import datetime
import calendar
import time

import serial

import cv2
import numpy as np

import bt
import socket
from gpiozero import Button

# The Video's Duration Before Dance
duration = 50

# Time & Serial Functions
def unix():
	d = datetime.utcnow()
	return calendar.timegm(d.utctimetuple())

ser = serial.Serial('/dev/ttyACM0', 9600)

def send(data):
	ser.write(bytes(str(data), 'utf-8') + b'\n')

# "PigSwitch"
hostname = socket.gethostname()
if hostname == "pigS":
	color = "red"
	
	minW = 20
	minH = 20

	maxW = 100
	maxH = 100
	
	IMAGE_FLIP = True
	b = Button(26)
	
else if hostname == "pigZ":
	color = "blue"
	
	minW = 20
	minH = 20

	maxW = 150
	maxH = 150

	IMAGE_FLIP = True
	
else if hostname == "pigM":
	color = "green"
	
	minW = 20
	minH = 20

	maxW = 100
	maxH = 100
	
	IMAGE_FLIP = False
	
else:
	print("HOSTFAULT")
	exit()
	
# The Color Switching Part
if color == "red":
	low = np.array([160, 80, 80])
	high = np.array([179, 255, 255])
else if color == "green":
	low = np.array([54, 85, 20])
	high = np.array([98, 255, 255])
else if color == "blue":
	low = np.array([90, 140, 50])
	high = np.array([134, 255, 255])
else:
	print("COLORFAULT")
	exit()
	
# OpenCV Stuff
cap = cv2.VideoCapture(-1)
cap.set(3, int(320))
cap.set(4, int(240))

ret, _ = cap.read()
if not ret:
	print("CAMFAULT")
	exit()

# The Bluetooth Magic
bt = bt.BT()
if hostname == "pigS":
	while (b.is_pressed):
		pass
	bt.start()
else:
	bt.sync()
	
# The Start Sequence
start = unix()
send(1000)
time.sleep(1)
send(1000)

# Main Loop
while True:
	ret, frame = cap.read()
	
	width = 0
	heigth = 0
        
	if (ret):
		if (IMAGE_FLIP):
			frame = cv2.flip(frame, 0)
			frame = cv2.flip(frame, 1)
		
		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(hsv_frame, low, high)
		contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

		for cnt in contours:
			(x, y, w, h) = cv2.boundingRect(cnt)
			width = w
			heigth = h
			if width > minW and heigth > minH:
				send(x)
			break
	
	cv2.waitKey(1)

	if ((width > maxW and heigth > maxH) or unix() - start > duration):
		break
	
while(unix() - start > 0):
	pass

# Finish Up
send(2000)

cap.release()
cv2.destroyAllWindows()
