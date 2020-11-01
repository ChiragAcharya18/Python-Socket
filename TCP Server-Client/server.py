import socket
import sys

s = socket.socket()
print("Socket Created")
name = socket.gethostname()
host = socket.gethostbyname(name)
print("Host: ",host)
s.bind((host, 9999))
s.listen(3)
print("Waiting for connection...")


while True:
    c, add = s.accept()
    msg = c.recv(1024).decode()
    if msg == "free" or not msg:
        print("Disconnecting... ")
        break
    print(f"Connected with IP: {add[0]} Port: {add[1]} \nMessage: {msg}")
    c.send(bytes("Welcome!", 'utf-8'))

s.close()