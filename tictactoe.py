import random

board = [[".",".","."],[".",".","."],[".",".","."]]
restart="y"
players = ["x", "o"]

def draw():
    print("\n  1 2 3")
    rowheaders="abc"
    row=""
    y=0
    for i in board:
        row+=rowheaders[y]+" "
        for j in i:
            row+=j+" "
        print(row)
        y+=1
        row=""
    print()

def control(selected, player):
    x=int(selected[0])
    y=int(selected[1])
    if(board[x][0]==player and board[x][1]==player and board[x][2]==player):
        print(player," Wins!")
        return False
    if(board[0][y]==player and board[1][y]==player and board[2][y]==player):
        print(player, "Wins!")
        return False
    if((board[0][0]==player and board[1][1]==player and board[2][2]==player) or (board[0][2]==player and board[1][1]==player and board[2][0]==player)):
        print(player, "Wins!")
        return False
    return True

def fill(selected, player):
    board[selected[0]][selected[1]]=player


def take(player):
        selected=[0,0]
        select_string = input("Select a dot ("+ player+"): ")
        if(select_string[0] in "aA"):
            selected[0]=0
        elif(select_string[0] in "bB"):
            selected[0]=1
        elif(select_string[0] in "cC"):
            selected[0]=2
        else:
            print("Faulty Input: " + select_string[0])
            return 0
        y = int(select_string[1])
        if(y not in [1,2,3]):
            print("Faulty Input: " + str(y))
            return 0
        selected[1]=y-1
        if(board[selected[0]][selected[1]]!="."):
            print("You can select only the dots!")
            return 0
        return selected

def game():
    global board
    board = [[".",".","."],[".",".","."],[".",".","."]]
    player=random.choice(players)
    endcheck=True
    turns=0
    while(endcheck):
        if(turns==9):
            print("Draw game")
            return
        draw()
        taken = take(player)
        while(taken==0):
            taken=take(player)
        selected=taken
        fill(selected,player)
        endcheck = control(selected, player)
        turns+=1
        if(player=="x"):
            player="o"
        else:
            player="x"


while(restart in "yY"):
    game()
    draw()
    restart = input("New Game?(yY) ")
