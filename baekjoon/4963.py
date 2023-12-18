import sys
sys.setrecursionlimit( 10 ** 6)

def dfs(y,x):

    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]

    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= nx < m and 0 <= ny < n and lands[ny][nx] == 1 and visited[ny][nx] == 0:
            visited[ny][nx] = 1 
            dfs(ny,nx)

while True:
    cnt = 0
    m,n = map(int,input().split())

    if m == n == 0:
        break
    lands = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0]  * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if lands[i][j] == 1 and visited[i][j] == 0: 
                visited[i][j] = 1
                cnt += 1
                dfs(i,j)
    print(cnt)

