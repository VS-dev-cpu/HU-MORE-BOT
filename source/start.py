import os
import time
import bt
from gpiozero import Button

def send(data):
    os.system("echo '" + str(data) + "\\n' >> /dev/ttyS0")

bt = bt.BT()

b = Button(26)
while (1):
        if not b.is_pressed:
                break

print("Starting...")
bt.start()

time.sleep(8)

print("Done")
send(1)
