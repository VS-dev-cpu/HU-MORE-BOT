# Konnichiwa!

from datetime import datetime
import calendar
import time

import os

import cv2
import numpy as np

import bt

# ---------- CONFIGURATION ----------
duration = 60	# The Searching's Duration
speedLimit = 0.05	# Limit the code's speed

size = 0	# The Acorn's Size
minSize = 150	# The Acorn's min size

low = np.array([161, 155, 84])	# Low Color HSV
high = np.array([179, 255, 255])	# High Color HSV

IMAGE_FLIP_VERTICALLY = False	# Flip the image VERTICALLY
IMAGE_FLIP_HORIZONTALLY = False	# Flip the image HORIZONTALLY
IMAGE_RESIZE = True	# Resize the image
W = 320	# The resized image's size
H = 240	

debugging = False	# Debugging the code

# ---------- NOITARUGIFNOC ----------

def unix():
	d = datetime.utcnow()
	return calendar.timegm(d.utctimetuple())

def send(data):
    os.system("echo '" + str(data) + "\\n' >> /dev/ttyS0")

cap = cv2.VideoCapture(-1)

if (IMAGE_RESIZE):
    cap.set(3, int(W))
    cap.set(4, int(H))
	
ret, _ = cap.read()
if not ret:
	print("CAMFAULT: CAN'T READ FROM THE CAMERA!")
	
if (ret and IMAGE_RESIZE and (W != cap.get(3) or H != cap.get(4))):
	print("CAMFAULT: CAN'T RESIZE IMAGE!")

W = cap.get(3)
H = cap.get(4)

bt = bt.BT()

bt.sync()
	
start = unix()
send(1)

while True:
	ret, frame = cap.read()
        
	# OpenCV Stuff
	size = 0
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
			size = int((w + h) / 2)
			break
    
	if debugging:
		cv2.imshow("frame", frame)
	
	# The EXIT stuff is happening here
	key = cv2.waitKey(1)
	if (key == 27):
		exit()
		
	if (size > minSize or unix() - start > duration):
		break
		
	time.sleep(speedLimit)
    
# And The Final Dance
send(2)

cap.release()
cv2.destroyAllWindows()

# Oyasumi!
