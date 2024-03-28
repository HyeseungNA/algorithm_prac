n,m,y,x,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
orders = list(map(int,input().split()))

dice = [0,0,0,0,0,0]

dy = [0,0,-1,1]
dx = [1,-1,0,0]

for order in orders:
    y += dy[order - 1]
    x += dx[order - 1]

    if 0 > y or y >= n or 0 > x or x >= m:
        y -= dy[order - 1]
        x -= dx[order - 1]
        continue
    else:
        if order == 1:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]


        elif order == 2:
            dice[0], dice[1], dice[2], dice[3], dice[4],dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
            

        elif order == 3:
            dice[0], dice[1], dice[2], dice[3], dice[4],dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]


        else:
            dice[0], dice[1], dice[2], dice[3], dice[4],dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]

        if board[y][x] == 0:
            board[y][x] = dice[0]
        
        else:
            dice[0] = board[y][x]
            board[y][x] = 0
    
        print(dice[5])


        