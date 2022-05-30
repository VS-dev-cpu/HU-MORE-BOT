import os
import time
import bt

bt = bt.BT()

def send(data):
    os.system("echo '" + str(data) + "\\n' >> /dev/ttyS0")
    
bt.sync()
time.sleep(8)
send(1)
