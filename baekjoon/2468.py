import sys
sys.setrecursionlimit(1000000)

n = int(input())
places = [list(map(int,input().split())) for _ in range(n)]
Max = 0
result = 0

def dfs(y,x,m):
    dy = [0, 0, -1, 1]
    dx =[1, -1, 0, 0]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n and visitied[ny][nx] == 0 and  places[ny][nx] > m:
            visitied[ny][nx] = 1
            dfs(ny,nx,m)


for i in range(n):
    for j in range(n):
        if Max < places[i][j]:
            Max = places[i][j]



for m in range(Max+1):
    visitied = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if places[i][j] > m and visitied[i][j] == 0:
                visitied[i][j] = 1
                cnt += 1
                dfs(i,j,m)

    result = max(result, cnt)

    
print(result)