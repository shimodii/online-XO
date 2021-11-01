#!/usr/bin/python3

# pyngrok
status=0
board=[[0,0,0],[0,0,0],[0,0,0]]

def print_board():
    for i in range(3):
        print ("|",end="")
        for j in range(3):
            print (board[i][j],end="")
            print ("|",end="")

        print ("")



def server():
    status=1


def client(address):
    status=0


print ("hello welcome to XO game!")
choice=input("""1- make a game!
        2- join a friend game!""")

print ("\n")

if choice == '2':
    addr=input("OK, enter friend game address: ")
    client(addr)
    

