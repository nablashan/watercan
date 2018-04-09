import socket
s=socket.socket()
host=socket.gethostname()
port=8080

s.connect((host,port))
print( s.recv(1024))
message=input("-:")
s.send(message.encode('utf-8'))

s.close
