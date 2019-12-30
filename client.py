 from socket import *
import json
import _pickle as pickle
import threading
import sys

class client:
    #defining protocols 
    peer_port_info = "peer_port_info"
    get_peers_info = "get_peers_info"
    file_upload = "file_upload"
    
    def __init__(self,p2p_server_addr,p2p_server_port,our_port,name):
        self.server_addr = p2p_server_addr
        self.server_Port = p2p_server_port
        self.peer_port = our_port
        self.name = name
        #to connect with server
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect((self.server_addr,self.server_Port))
        data = pickle.dumps([self.peer_port_info,self.name,self.peer_port])
        self.socket.sendall(data)
        hello = self.socket.recv(5012)
        print(hello.decode())
        # self.get_peer_info()
        # self.get_peer_info()
        # print(self.clientSocket)
        #to connect with this peer
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.bind(('',self.peer_port))

        t2 = threading.Thread(target = self.menu)
        t2.start()
        print("------------------------------------------")
        # print(self.clientSocket.getsockname())
        print("------------------------------------------")
        self.clientSocket.listen(4)
        print("i am here help me")
        client_conn, addr = self.clientSocket.accept()
        t1 = threading.Thread(target = self.listenToclient,args = (client_conn,addr))
        t1.start()
            # t1.join()


    def listenToclient(self,client_conn,addr):
        # self.add_peers(client_conn,addr)

        fileName = client_conn.recv(1024).decode()
        print(fileName)
        print("enter q to quit")
        if(fileName != "q"):
            msg = input("\nenter your msg ")
            client_conn.send(msg.encode())
            self.listenToclient(client_conn,addr)
            # client_conn.send(self.dict_to_binary(self.peer))    


    def display_info(self,info):
        print(info)
    
    def get_peer_info(self):
        data = pickle.dumps([self.get_peers_info])
        self.socket.sendall(data)
        print("i am here")
        peer_info = self.socket.recv(5555012)
        if peer_info == b'':
            print("emptyy")
            peer_info = self.socket.recv(5555012)
            print(peer_info)
        else:
            print(pickle.loads(peer_info))

    def connect(self):
        self.new_Sock = socket(AF_INET, SOCK_STREAM)
        port = int(input("enter port no"))
        self.new_Sock.connect((self.server_addr,port))
        self.talk()

    def talk(self):
        self.new_Sock.send(("hello from"+self.name).encode())
        while True:
            print("waiting for reply \n")
            fileName = self.new_Sock.recv(1024).decode()
            print(fileName)
            print("enter q to quit \n")
            if(fileName != "q"):
                msg = input(" \n enter your msg ")
                self.new_Sock.send(msg.encode())
            else:
                break

    def upload_file(self):
        fname = input("enter file name : ")
        data = pickle.dumps([self.upload_file,fname,self.peer_port])
        self.socket.sendall(data)
        hello = self.socket.recv(5012)
        print(hello.decode())
        
    def menu(self):
        while True:
            
            print(" \n Hello World")
            user_input = input("enter 'show peers' to see the peers list \n enter 'connect' to connect to peer \n enter 'upload file' to upload file  \n")
            if user_input == "show peers":
                self.get_peer_info()
            if user_input == "connect":
                self.connect()
            if user_input == "upload file":
                self.upload_file()

    # message = input("client:: enter your message ")
    # clientSocket.send(message.encode())
    # modifiedMessage = clientSocket.recv(1024)
    # print('from server: ', modifiedMessage.decode())
    # .clientSocket.close()
name = sys.argv[1]
our_port = int(sys.argv[2])
p2p_server_addr = sys.argv[3]
p2p_server_port = int(sys.argv[4])
c = client(p2p_server_addr,p2p_server_port,our_port,name)


