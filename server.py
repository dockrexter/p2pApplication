from socket import *
import threading

class server:
    serverPort = 7004
    
    def __init__(self):
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(('',self.serverPort))
        serverSocket.listen(10)
        while True:
            client_conn, addr = serverSocket.accept()
            client_conn.settimeout(60)
            threading.Thread(target = self.listenToclient,args = (client_conn,addr)).start()
    def add_peers(self,client_conn,addr):
        peer = {}



    def listenToclient(self,client_conn,addr):
        self.add_peers(client_conn,addr)
        fileName = client_conn.recv(1024).decode()
        print("message recv from client_conn: ", fileName)
        fileName = fileName.upper()
        client_conn.send(fileName.encode())
        client_conn.close()

    
    
server = server()


