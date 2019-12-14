from socket import *
serverName = 'localhost'
serverPort = 7004
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = input("client:: enter your message ")
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(1024)
print('from server: ', modifiedMessage.decode())
clientSocket.close()
