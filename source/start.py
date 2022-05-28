import os
import time
import bt
from gpiozero import Button

bt = bt.BT()

def send(data):
    os.system("echo '" + str(data) + "\\n' >> /dev/ttyS0")

b = Button(26)
while (b.is_pressed):
    pass

bt.start()
time.sleep(8)
send(1)
