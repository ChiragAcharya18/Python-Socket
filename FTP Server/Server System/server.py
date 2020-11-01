import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
s.bind((host, 12345))
s.listen(3)
print("Waiting for Connection...")
c, a = s.accept()
print("Connection Established: ",a)

fn = input("Enter File name: ")
if fn[-4:] != ".txt":
    fn = fn + ".txt"

fh = open(fn, 'rb')
fd = fh.read(1024)
c.send(fd)

print("Sent Successfully!")
d1 = c.recv(1024).decode('utf-8')
print("Client Acknowledgement: ",d1)

s.close()

