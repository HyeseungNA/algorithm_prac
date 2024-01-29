from collections import deque

def bfs(y,x):
    total= 0
    c = [[0] * m for _ in range(n)]
    c[y][x] = 1
    q = deque()
    q.append([y,x])

    while q:
        y,x = q.popleft()
        dy = [-1,0,1,0]
        dx = [0,-1,0,1]


        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if c[ny][nx] == 0 and graph[ny][nx] == 'L':
                    c[ny][nx] = c[y][x] + 1
                    total = max(total, c[ny][nx])
                    q.append([ny,nx])
                
    return total - 1


n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result = 0
Max = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            result = bfs(i,j)
            Max = max(result,Max)

print(Max)
