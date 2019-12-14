from socket import *
import threading



def listenToClient(client,addr):
    message = client.recv(1024).decode()
    print("message recv from client: ", message)
    message = message.upper()
    client.send(message.encode())
    client.close()



serverPort = 7001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(10)
print("the server is ready to recieve ")
while True:
    client, addr = serverSocket.accept()
    client.settimeout(60);
    threading.Thread(target = listenToClient,args = (client,addr)).start()



