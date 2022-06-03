import bt
import serial

bt = bt.BT()
ser = serial.Serial('/dev/ttyS0', 9600)
    
bt.sync()
ser.write(b'1\n')
