import socket
import xml.etree.ElementTree as ET
#Run this file after running the gazepointer application

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",43333)) #connect to the socket

s.send("xml\n".encode("utf-8"))#Send data format
print(s.send('AppKeyDemo\n'.encode("utf-8"))) #Send AppKey
#s.settimeout(1.0)


while True:
    data = s.recv(4096)
    try:
        data = data.decode("utf-8")
    except:
        continue
    
    
    print(data)
    try:
        root = ET.fromstring(data[1:])
    except:
        continue
    print(root)
    print("heymama-------------------------------------------------------------------------------")
