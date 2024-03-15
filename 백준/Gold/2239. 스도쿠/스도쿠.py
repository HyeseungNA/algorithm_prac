import sys

def sero(x,num):
    
    for i in range(9):
        if board[i][x] == num:
            return False
        
    return True


def garo(y,num):
    for i in range(9):
        if board[y][i] == num:
            return False

    return True
def zig(y,x,num):
    
    now_y = (y // 3) * 3
    now_x = (x // 3) * 3

    for i in range(now_y, now_y + 3):
        for j in range(now_x, now_x + 3):
            if board[i][j] == num:
                return False

    return True



def dfs(n):
    global blank

    if n == len(blank):
        for b in board:
            print(*b,sep="")
        exit()
    
    for i in range(1,10):
        y = blank[n][0]
        x = blank[n][1]
        if sero(x,i) and garo(y,i) and zig(y,x,i):
            board[y][x] = i
            dfs(n+1)
            board[y][x] = 0
        



board = [list(map(int,input())) for _ in range(9)]
numbers = [0,1,2,3,4,5,6,7,8,9]
# print(board)
blank = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append([i,j])


dfs(0)