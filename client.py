from socket import *
import json
class client:
    serverName = '127.0.0.1'
    serverPort = 8951
    def __init__(self):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((self.serverName,self.serverPort))
        message = "1"
        clientSocket.send(message.encode())
        while True: 
            info = clientSocket.recv(1024)
            self.display_info(self.binary_to_dict(info))

    def display_info(self,info):
        print(info)
    def dict_to_binary(self,the_dict):
        str = json.dumps(the_dict)
        binary = ' '.join(format(ord(letter), 'b') for letter in str)
        return binary


    def binary_to_dict(self,the_binary):
        jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
        d = json.loads(jsn)  
        return d

    # message = input("client:: enter your message ")
    # clientSocket.send(message.encode())
    # modifiedMessage = clientSocket.recv(1024)
    # print('from server: ', modifiedMessage.decode())
    # .clientSocket.close()
c = client()