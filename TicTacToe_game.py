# Empty board
board=["#"," "," "," "," "," "," "," "," "," "]
#store the position of the board
a=[]
# function to display the board
def display_board(board):
    print("   "+"|"+"   "+"|"+"   ")
    print(" "+board[1]+" "+"|"+" "+board[2]+" "+"|"+" "+board[3])
    print("   "+"|"+"   "+"|"+"   ")
    print("-----------")
    print("   "+"|"+"   "+"|"+"   ")
    print(" "+board[4]+" "+"|"+" "+board[5]+" "+"|"+" "+board[6])
    print("   "+"|"+"   "+"|"+"   ")
    print("-----------")
    print("   "+"|"+"   "+"|"+"   ")
    print(" "+board[7]+" "+"|"+" "+board[8]+" "+"|"+" "+board[9])
    print("   "+"|"+"   "+"|"+"   ")


#Selecting Design for player
def player_design():
    player1=" "
    while player1 not in ["X","O"]:
        player1=input("Player1 select any one form X,O : ").upper()
    if player1=="X":
        player2="O"
    else:
        player2="X"
    return player1,player2

#Input Position function
def position():
    i=" "
    while i not in ["1","2","3","4","5","6","7","8","9"]:
        i=input("enter the position from (1-9) : ")
    i=int(i)
    if (len(a)==0):
        a.append(i)
        return i
    while i in a:
        i=input("Entered position is already taken so select new position : ")
        i=int(i)
        a.append(i)
        break
    while i not in a:
        a.append(i)
        break
    return i

#to watch the player
def choose():
    if len(a)%2==1:
        return 1
    elif len(a)%2==0:
        return 2

#save the move   
def move(player_number,position,board,design1,design2):
    if player_number==1:
        board[position]=design1
    elif player_number==2:
        board[position]=design2
    display_board(board)

def play(mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def result():
    result1=play(player1)
    result2=play(player2)
    if result1:
         print("Player1 Wins the match ")
         return 1
    elif result2:
        print("Player2 wins the match")
        return 1
    elif(len(a)==9):
        print("Match Tie")
        return 1
display_board(board)
player1,player2=player_design()
def start():
    for i in range(0,9):
        pos=position()
        player=choose()
        move(player,pos,board,player1,player2)
        res=result()
        if res:
            i
            break
            
start()
while (True):
    i=""
    while i not in ["Y","N"]:
        i=input("Enter 'Y' to restart or 'N' exit : ").capitalize()
    if (i=="Y"):
        board=["#"," "," "," "," "," "," "," "," "," "]
        a=[]
        display_board(board)
        player1,player2=player_design()
        start()
    else:
        break
