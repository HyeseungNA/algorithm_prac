
from collections import deque


def bfs(x,y):
    global cnt
    q = deque()
    q.append(adj[y][x])


    while q:
        q.popleft()
        cnt += 1

        #다음노드
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            #범위
            if nx < 0 or nx >= M or ny < 0 or ny >= N or adj[ny][nx] == 0:
                continue

            q.append(adj[ny][nx])
    return cnt



N,M = map(int,input().split())

adj = []
cnt = 0
for _ in range(N):
    adj.append(list(map(int,input())))




print(bfs(1,1))


