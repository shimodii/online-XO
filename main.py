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


def client():
    status=0
