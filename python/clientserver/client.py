import socket
s=socket.socket()
host=socket.gethostname()
port=8080
s.connect((host,port))
while 1:
     print("Connected to chat server")
     msg=(s.recv(1024)).decode('utf-8')
     if msg=="b":
        break
     else:
       print(msg)
     #print( s.recv(1024))
       message=input("-:")
       s.send(message.encode('utf-8'))
       print("message has been sent")


