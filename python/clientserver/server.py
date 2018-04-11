import socket


s = socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
s.listen(5)
(client,(ip,port))=s.accept()

while 1:
      addr=(ip,port)
      print ("got connection fron:", addr)
      print(" Enter b for exit")
      message=input('->')
      if message=="x":
            exit()
      else:
          print(message.encode())
          client.send(message.encode('utf-8'))
          print("message has been sent")
          print(client.recv(1024))
