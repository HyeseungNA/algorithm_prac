
from collections import deque


def bfs(x,y,cnt):
    q = deque()
    #y좌표, x좌표, 이동거리
    q.append((y,x,cnt))
    visited[y][x] = 1


    while q:
        y,x,cnt = q.popleft()
        if (y == N-1 and x == M-1):
            return cnt


        #다음노드
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            #범위 벗어나면 넘어가
            if nx < 0 or nx >= M or ny < 0 or ny >= N or adj[ny][nx] == 0:
                continue
            #방문 안했으면 큐에 넣어
            if visited[ny][nx] == 0:
                q.append((ny,nx,cnt+1))
                visited[ny][nx] =  1
    

    return 



N,M = map(int,input().split())

adj = []
visited = [[0]*M for _ in range(N)]


for _ in range(N):
    adj.append(list(map(int,input())))


print(bfs(0,0,1))



