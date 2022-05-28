import os
import time
import bt
from gpiozero import button

def send(data):
    os.system("echo '" + str(data) + "\\n' >> /dev/ttyS0")

bt = bt.BT()

b = Button(26)

while (1):
        if not b.is_pressed:
                break

#time.sleep(0)

bt.start()

send(1)
