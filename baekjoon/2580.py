def dfs(n):
    numbers = [1,2,3,4,5,6,7,8,9]
    if n == len(blank):
        for b in board:
            print(*b)
        exit()


    y = blank[n][0]
    x = blank[n][1]
    for num in numbers: 
        if sero(x,num) and garo(y,num) and square(y,x,num):
            board[y][x] = num
            dfs(n+1)
            board[y][x] = 0


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


def square(y,x,num):
    ny = y // 3
    nx = x // 3
   
    for i in range(ny * 3, (ny + 1) * 3):
        for j in range(nx * 3 , (nx + 1) * 3):
            if board[i][j] == num:
                return False
    return True

board = [list(map(int,input().split())) for _ in range(9)]

blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append([i,j])

             
dfs(0)  




'''
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

'''