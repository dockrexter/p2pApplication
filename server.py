from socket import *
import threading
import random
import json
class server:
    
    serverPort = random.randint(7000,9000)
    print(serverPort)
    peer = {}
    def __init__(self):
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(('',self.serverPort))
        serverSocket.listen(10)
        while True:
            client_conn, addr = serverSocket.accept()
            print(addr)
            client_conn.settimeout(60)
            threading.Thread(target = self.listenToclient,args = (client_conn,addr)).start()
    def add_peers(self,client_conn,addr):
        self.peer[client_conn] = addr




    def listenToclient(self,client_conn,addr):
        self.add_peers(client_conn,addr)
        fileName = client_conn.recv(1024).decode()
        if(fileName == "1"):
            while True:
                print(self.peer.values())
                client_conn.send(self.dict_to_binary(self.peer.values()))      
        # print("message recv from client_conn: ", fileName)
        # fileName = fileName.upper()
        # client_conn.send(fileName.encode())
        # print(self.peer)
        # self.client_conn.close()

    def dict_to_binary(self,the_dict):
        str = json.dumps(the_dict)
        binary = ' '.join(format(ord(letter), 'b') for letter in str)
        return binary


    def binary_to_dict(self,the_binary):
        jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
        d = json.loads(jsn)  
        return d

    
    
server = server()


