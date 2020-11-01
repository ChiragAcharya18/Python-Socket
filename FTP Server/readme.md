This is basically a simple file transfer system with the help of Python socket.
Server is the one that sends the file. User has to input the name of the file to be sent. The file is read in bytes mode and the it is sent to client.
The client creates a file with name as inputed by the user and the recieved data is written to that file. An acknowledgement message that file is recieved is sent to the server.
