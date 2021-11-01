#!/usr/bin/python3


import socket
import pickle 
fr60 pyngrok import ngrok 

status=1 # set 0 for client and 1 for server (for turns)
board=[[0,0,0],[0,0,0],[0,0,0]] # main board
geo={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}

def turn_guide():
    print ("this is guid for turns and inputs:")
    for i in range(1,10):
        if i%3!=0:
            print (i,end="|")
        else:
            print (i,end="\n")


def print_board() :
    for x in range(len(board)) : 
        for y in range(len(board[x])) : 
            if y == 2 :
                print(board[x][y] , end = "\n")
                if x != 2 :
                    print("----------")
            else : 
                print(board[x][y] , end = " | ")


#
class prcess : 
    def __init__(self , connection_type , ip = None , port = None) :
        self.server_config = ((ip , port)) 
         
        if connection_type == "host" : 
            self.server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            self.server_socket.bind(self.server_config)
            print("server started . . . ")
            tcp_link = ngrok.connect(ip , "tcp").public_url
            print(f"link : {tcp_link}")
            self.server_socket.listen(1)
            self.client , self.client_info = self.server_socket.accept()
            print(f"{self.client_info} has connected to the server")

        elif connection_type == "client" : 
            self.server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            self.server_socket.connect(self.server_config)

    
    def send_data_c(self , board_data) :
        board_data = pickle.dumps(board_data)
        self.server_socket.send(board_data) 


    def send_data_h(self , board_data) : 
        board_data = pickle.dumps(board_data)
        self.client.send(board_data)



    def get_data(self , type ) : 
        if type == "host" : 
            socket_connection = self.client

        elif type == "client" :
            socket_connection = self.server_socket

        else : return "There is a problem for get type connection" # this return help is for prevent any error 
        
        board_data = socket_connection.recv(4096)
        return pickle.loads(board_data)
    
        


print ("hello welcome to XO game!")
choice=input("""1- make a game!
        2- join a friend game!""")

print ("\n")

    

