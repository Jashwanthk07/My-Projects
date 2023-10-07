import numpy as np
b=np.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1='X'
p2='O'
def check_rows(symbol):

    for r in range(3):
        count=0
        for c in range(3):
            if b[r][c]==symbol:
                count+=1
            if count==3:
                print(symbol,'Wins')
                return True
    return False
def check_columns(symbol):

    for c in range(3):
        count=0
        for r in range(3):
            if b[r][c]==symbol:
                count+=1
            if count==3:
                print(symbol,'Wins')
                return True
    return False
def check_diagonals(symbol):
    if b[0][2]==b[1][1] and b[1][1]==b[2][0] and b[1][1]==symbol:
        print(symbol,'Wins')
        return True
    if b[0][0]==b[1][1] and b[1][1]==b[2][2] and b[1][1]==symbol:
        print(symbol,'WIns')
        return True
    return False
def wins(symbol):
    return check_diagonals(symbol) or check_columns(symbol) or check_rows(symbol)
def place(symbol):
    print(np.matrix(b))
    while(1):
        row=int(input('Enter the row -1 or 2 or 3:'))
        col=int(input('Enter the column- 1 or 2 or 3:'))
        if row>0 and row<4 and col>0 and col<4 and b[row-1][col-1]=='-':
            break
        else:
            print('Invalid input entered')
    b[row-1][col-1]=symbol

def play():
    for turn in range(9):
        if turn%2==0:
            print('X turn' )
            place(p1)
            if wins(p1):
                break
        else:
            print('O turn')
            place(p2)
            if wins(p2):
                break
    if not(wins(p1)) and not(wins(p2)):
        print('Its a draw')

play()
