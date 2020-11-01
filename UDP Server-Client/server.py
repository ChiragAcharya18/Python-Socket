import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('localhost',12345))
print("Waiting for Connection...")
while True:
    d1, a1 = s.recvfrom(1024)
    d2, a2 = s.recvfrom(1024)
    print("{0}>\t{1}".format(d1.decode(),d2.decode()))

    if d1.decode()=="admin" and d2.decode() == "free":
        print("Hello Admin!")
        print("Closing Server..")
        s.close()
        sys.exit()

    msg = "Hello! This is UDP Server. Your Message is recieved."
    s.sendto(msg.encode('utf-8'), a1)

