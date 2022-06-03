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
duration = 60	# The Searching's Duration
speedLimit = 0.05	# Limit the code's speed

minW = 100	# The Acorn's Min Width
minH = 100	# The Acorn's min Heigth

low = np.array([160, 100, 84])  # Low Color HSV
high = np.array([179, 255, 255])        # High Color HSV

IMAGE_FLIP_VERTICALLY = True	# Flip the image VERTICALLY
IMAGE_FLIP_HORIZONTALLY = True	# Flip the image HORIZONTALLY

# ---------- NOITARUGIFNOC ----------

# Functions
def unix():
	d = datetime.utcnow()
	return calendar.timegm(d.utctimetuple())

def send(data):
    os.system("echo '" + str(data) + "\\n' >> /dev/ttyS0")

# Init
cap = cv2.VideoCapture(-1)
cap.set(3, int(320))
cap.set(4, int(240))
	
ret, _ = cap.read()
if not ret:
	print("CAMFAULT: CAN'T READ FROM THE CAMERA!")

W = cap.get(3)
H = cap.get(4)

bt = bt.BT()

# The Magic BT Sync Stuff
if socket.gethostname() == "pigS":
	b = Button(26)
	while (b.is_pressed):
		pass
	#bt.start()
else:
	bt.sync()

start = unix()

# Main Loop
while True:
	ret, frame = cap.read()
        
	# OpenCV Stuff
	width = 0
	heigth = 0
	if (ret):
		if (IMAGE_FLIP_VERTICALLY):
			frame = cv2.flip(frame, 0)
		if (IMAGE_FLIP_HORIZONTALLY):
			frame = cv2.flip(frame, 1)
		
		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(hsv_frame, low, high)
		contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

		# Getting The Acorn's size
		for cnt in contours:
			(x, y, w, h) = cv2.boundingRect(cnt)
            if x > (W / 2 + W / 10):
                send(3)
            if x < (W / 2 - W / 10):
                send(4)
			width = w
			heigth = h
			break
	
	# The EXIT stuff is happening here
	cv2.waitKey(1)

	if ((width > minW and heigth > minH) or unix() - start > duration):
		break
	
# Finish Up
send(2)

cap.release()
cv2.destroyAllWindows()
