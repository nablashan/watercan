import socket


s = socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
s.listen(5)
while True:
 (client,(ip,port))=s.accept()
 addr=(ip,port)
 print ("got connection fron:", addr)
   
 message=input('->')
 client.send(message.encode('utf-8'))
 print(client.recv(1024))
 client.close
