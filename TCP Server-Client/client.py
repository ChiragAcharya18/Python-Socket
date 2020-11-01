import socket
import sys

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
c.connect(('192.168.56.1',9999))

msg = input("Enter message: ")

c.send(msg.encode('utf-8'))
data = c.recv(1024).decode('utf-8')
print("Recieved Data: ", data)
c.close()