from collections import deque
def bfs(y,x,lst):
    global flag,cnt
    
    dy = [-1,0,1,0]
    dx = [0,-1,0,1]

    q = deque()
    q.append([y,x])

    while q:
        y,x = q.popleft()
        now = board[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if Min <= abs(board[ny][nx] - now) <= Max and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    lst.append([ny,nx,board[ny][nx]])
                    q.append([ny,nx])
    
    if len(lst) != 1:
        total = 0
        for el in lst:
            total += el[2]
        
        for y,x,cost in lst:
            board[y][x] = total // len(lst)
        
      
        flag = 1
    

n, Min, Max = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dy = [0,-1,0,1]
dx = [-1,0,1,0]

cnt = 0

while True:
    flag = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i,j,[[i,j,board[i][j]]])
    
    if flag == 1:
        cnt += 1
    if flag == 0:
        break
print(cnt)