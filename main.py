#!/usr/bin/python3

# pyngrok
status=1 # set 0 for client and 1 for server (for turns)
board=[[0,0,0],[0,0,0],[0,0,0]] # main board
geo={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}

def print_board() :
    for x in range(len(board)) : 
        for y in range(len(board[x])) : 
            if y == 2 :
                print(board[x][y] , end = "\n")
                if x != 2 :
                    print("----------")
            else : 
                print(board[x][y] , end = " | ")



def server():
    while 1:
        if status != 1:
            pass

        if status == 1:
            turn=int(input("it's your turn!: "))


def client(address):
    while 1:
        if status == 1:
            pass
        
        if status != 1:
            turn=int(input("it's your turn!: "))

print ("hello welcome to XO game!")
choice=input("""1- make a game!
        2- join a friend game!""")

print ("\n")

if choice == '2':
    addr=input("OK, enter friend game address: ")
    client(addr)
    

