# The Code For The Pigs

from datetime import datetime
import calendar
import time

import os

import cv2
import numpy as np

import bt
import socket
from gpiozero import Button

# ---------- CONFIGURATION ----------
duration = 50
speedLimit = 0

minW = 5
minH = 5

maxW = 100
maxH = 100

low = np.array([160, 80, 80])
high = np.array([179, 255, 255])

IMAGE_FLIP_VERTICALLY = True
IMAGE_FLIP_HORIZONTALLY = True
# ---------- NOITARUGIFNOC ----------

# Functions
def unix():
	d = datetime.utcnow()
	return calendar.timegm(d.utctimetuple())

def send(data):
	port = '/dev/ttyS0'
    os.system("echo '" + str(data) + "\\n' >> " + port)

# OpenCV Stuff
cap = cv2.VideoCapture(-1)

cap.set(3, int(320))
cap.set(4, int(240))

W = cap.get(3)
H = cap.get(4)

ret, _ = cap.read()
if not ret:
	print("CAMFAULT")
	exit()

# The Bluetooth Magic
bt = bt.BT()

if socket.gethostname() == "pigS":
	b = Button(26)
	while (b.is_pressed):
		pass
	bt.start()
else:
	bt.sync()

start = unix()

send(1000)
time.sleep(5)
sleep(1000)

# Main Loop
while True:
	ret, frame = cap.read()
        
	if (ret):
		if (IMAGE_FLIP_VERTICALLY):
			frame = cv2.flip(frame, 0)
		if (IMAGE_FLIP_HORIZONTALLY):
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
