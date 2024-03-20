from collections import deque

def bfs():
    global result
    while q:
        y,x,punch = q.popleft()
        if y == n - 1 and x == m - 1:
            result = visited[y][x][punch]
            break


        dy = [-1,0,1,0]
        dx = [0,-1,0,1]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                
                if graph[ny][nx]  == 0 and visited[ny][nx][punch] == 0:
                    visited[ny][nx][punch] = visited[y][x][punch] + 1
                    q.append([ny,nx,punch])
                
                elif graph[ny][nx] == 1 and punch == 0:
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    q.append([ny,nx,1])
                


n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
q = deque()
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
result = -1
q.append([0,0,0])
visited[0][0][0] = 1
bfs()

print(result)
'''
9 9
010001000
010101010
010101010
010101010
010101010
010101010
010101010
010101011
000100010
'''