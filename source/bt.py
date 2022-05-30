import os
import bluetooth
from time import sleep

class BT():
    def __init__(self):
        os.system("bluetoothctl discoverable on")
        
        self.mac_rooster = "B8:27:EB:48:52:95"  #Final (RPi0)
        self.mac_pigS = "DC:A6:32:6B:3A:AB" #Final (RPi4) [SERVER]
        self.mac_pigZ = "DC:A6:32:6E:92:A5" #Final (RPi4)
        self.mac_pigM = "B8:27:EB:10:0D:19" #Final (RPi3)
        
    def receive(self):
        server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
          
        port = 1
        server_sock.bind(("",port))
        server_sock.listen(1)
          
        client_sock,address = server_sock.accept()
          
        data = client_sock.recv(1024)
          
        client_sock.close()
        server_sock.close()
          
        return address[0], data;
      
    def send(self, targetBluetoothMacAddress, message):
        try:
            sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
            sock.connect((targetBluetoothMacAddress, 1))
            sock.send(message)
            sock.close()
            return True
        except:
            print("Failed to send message " + str(message) + " to " + str(targetBluetoothMacAddress))
            return False
        
    def sync(self):
        return self.receive()

    def start(self):
        self.send(self.mac_rooster, "go")
        self.send(self.mac_pigZ, "go")
        self.send(self.mac_pigM, "go")
