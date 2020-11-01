import socket

c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

name = input("Enter name: ")
c.sendto(name.encode('utf-8'),('localhost',12345))
msg = input("Enter message to be sent: ")
c.sendto(msg.encode('utf-8'),('localhost',12345))
if name != "admin" and msg != "free":
    data, addr = c.recvfrom(1024)
    print("Server: ", data.decode())
c.close()
