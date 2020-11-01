import socket
import sys

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket created successfully")
#print("Default timeout ",str(c.gettimeout()))
#c.settimeout(50)
#print("Current timeout ",str(c.gettimeout()))

try:                                                                                                                                                                                                                                                                                                                                                                        
    c.connect(('localhost',12345))
    print("Connected...")
except socket.timeout as E:
    print("Timeout Error: ",str(E))
    sys.exit()
except socket.error as E:
    print("Connect Error: ",str(E))
    sys.exit()
except TypeError as msg:
    print("TypeError: ",str(E))
    sys.exit()


fn = input("Enter the filename : ")
fn = fn + ".txt"
file = open(fn,'wb')
fd = c.recv(1024)
file.write(fd)
file.close()
ack = "File Recieved! Thankyou"
c.send(ack.encode('utf-8'))
print("File is recieved! ")

c.close()
