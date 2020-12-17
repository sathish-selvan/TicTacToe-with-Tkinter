from tkinter import *
from tkinter.messagebox import showinfo
root = Tk()
board=[[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]
    


def clear_board(board):
    board=[[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]
    return board
       
def monitor():
    
    global board
    
    for i in range(0,3): # to check horizontal
        if board[i][0] == "X"  and board[i][1] == "X" and board[i][2]=="X":
            print("player1 won the match")
            showinfo("RESULT","player1 won the match")
            return 1
        elif board[0][i] == "X"  and board[1][i] == "X" and board[2][i] =="X":#check vertical
            print("player1 won the match")
            showinfo("RESULT","player1 won the match")
            return 1
    if board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
        print("player1 won the match")
        showinfo("RESULT","player1 won the match")
        return 1
    if board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
        print("player1 won the match")
        showinfo("RESULT","player1 won the match")
        return 1
    
    for i in range(0,3): # to check horizontal
        if board[i][0] == "O"  and board[i][1] == "O" and board[i][2]=="O":
            print("player2 won the match")
            showinfo("RESULT","player2 won the match")
            return 1
        elif board[0][i] == "O"  and board[1][i] == "O" and board[2][i] =="O":#check vertical
            print("player2 won the match")
            showinfo("RESULT","player2 won the match")
            return 1
    if board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
        print("player2 won the match")
        showinfo("RESULT","player2 won the match")
        return 1
    if board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O":
        print("player2 won the match")
        showinfo("RESULT","player2 won the match")
        return 1
    return 0

def print_board():
    global board
    for i in range(0,3):
        
        print("-------------")
        line='| '
        for j in range(0,3):
            line += ''
            line += board[i][j]+" | " 
        print(line)
    print("-------------")


end_move = 0
player = 1
total_moves=0    
print_board()
def define_sign(number):

    global board,b1,b2,b3,b4,b5,b6,b7,b8,b9,end_move,player,total_moves
    
    
    
    moves = {1:"00",2:"01",3:"02",4:"10",5:"11",6:"12",7:"20",8:"21",9:"22"}
    butt = {1:"b1",2:"b2",3:"b3",4:"b4",5:"b5",6:"b6",7:"b7",8:"b8",9:"b9"}
    
    
        
    
    
    if player == 1:
        hope = int(number)
        p1_input = moves[hope]
        a = int(p1_input[0])
        b = int(p1_input[1])
        

        if board[a][b] == " ":
            board[a][b] = "X"
            eval(butt[hope]+".config(text='X')")
            print_board()
            player = 2
            
        else:
            print("invalid input, try again ")
                
        
    else:
        
        hope = int(number)
        p2_input = moves[hope]
        c = int(p2_input[0])
        d = int(p2_input[1])
        if board[c][d] == " ":
            board[c][d] = "O"
            eval(butt[hope]+".config(text='O')")
            print_board()
            player = 1
            
        else:
            print("invalid input, try again ")
                
        
    total_moves += 1
    
    print_board()
    if total_moves == 9:
        print("No one wins")
    end_move = monitor()
    if total_moves == 9 or end_move==1:
        board = clear_board(board)
        print_board()
        total_moves=0  
        b1.config(text=" ")
        b2.config(text=" ")
        b3.config(text=" ")

        b4.config(text=" ")
        b5.config(text=" ")
        b6.config(text=" ")

        b7.config(text=" ")
        b8.config(text=" ")
        b9.config(text=" ")


l1 = Label(root, text="Player 1 : X", font ="time 15")
l1.grid(row=0,column=1)
l2 = Label(root, text="Player 2 : O", font ="time 15")
l2.grid(row=0,column=2)

b1 = Button(root, width=20,height=10,command=lambda:define_sign(1))
b1.grid(row=1,column=1)
b2 = Button(root, width=20,height=10,command=lambda:define_sign(2))
b2.grid(row=1,column=2)
b3 = Button(root, width=20,height=10,command=lambda:define_sign(3))
b3.grid(row=1,column=3)

b4 = Button(root, width=20,height=10,command=lambda:define_sign(4))
b4.grid(row=2,column=1)
b5 = Button(root, width=20,height=10,command=lambda:define_sign(5))
b5.grid(row=2,column=2)
b6 = Button(root, width=20,height=10,command=lambda:define_sign(6))
b6.grid(row=2,column=3)

b7 = Button(root, width=20,height=10,command=lambda:define_sign(7))
b7.grid(row=3,column=1)
b8 = Button(root, width=20,height=10,command=lambda:define_sign(8))
b8.grid(row=3,column=2)
b9 = Button(root, width=20,height=10,command=lambda:define_sign(9))
b9.grid(row=3,column=3)

root.mainloop()

