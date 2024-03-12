from collections import deque

def bfs(y,x):
    cnt = 1
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
                if graph[ny][nx] == 0:
                    graph[ny][nx] += 1
                    cnt += 1
                    q.append([ny,nx])
    return cnt



n,m,k = map(int,input().split())
graph = [[0] * m for _ in range(n)]
lst = []
for _ in range(k):
    st_x,st_y,ed_x,ed_y = map(int,input().split())
    for i in range(st_y,ed_y):
        for j in range(st_x,ed_x):
            graph[i][j] += 1


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            graph[i][j] = 1
            result = bfs(i,j)
            lst.append(result)
print(len(lst))
lst.sort()
print(*lst)