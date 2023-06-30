# bfs로 풀기

from collections import deque

T = int(input())
for t in range(T):
    
    def bfs(s_x,s_y,cnt):


        while True:
            s_x,s_y,cnt = q.popleft()


            # 나이트가 목표 지점에 도착하면 cnt를 return 
            if s_x == e_x and s_y == e_y:
                return cnt


            # 나이트가 갈 수 있는 경로
            dy = [-2 ,-2, 2, 2, -1, -1, 1, 1]
            dx = [1, -1, 1, -1, 2, -2, 2, -2]
            
            for i in range(8):
                ny = s_y + dy[i]
                nx = s_x + dx[i]
                # 범위 안에 있고 방문도 안했으면
                if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0:
                    visited[ny][nx] = 1 # 방문처리하고
                    q.append([nx,ny,cnt+1]) # q에 넣어주기


    n = int(input())
    visited = [[0] * n for _ in range(n)]
    q = deque()
    s_x,s_y = map(int,input().split())
    e_x, e_y = map(int,input().split())
    visited[s_y][s_x] = 0
    q.append([s_x,s_y,0])

    result = bfs(s_x,s_y,0)
    print(result)