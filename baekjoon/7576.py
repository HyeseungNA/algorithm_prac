from collections import deque


def bfs():

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while q:
        y, x, cnt = q.popleft()
        graph[y][x] = cnt

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # 방문 안하고, 안 익었으면
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and graph[ny][nx] == 0:
                # cnt 추가해주고
                # cnt += 1
                # 방문 표시해주고
                visited[ny][nx] = 1
                q.append([ny, nx, cnt + 1])

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

q = deque()


# 토마토가 익은 곳 q에 넣기
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            visited[y][x] = 1
            q.append([y, x, 1])
            graph[y][x] = 1


def result(graph):
    MAX = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return -1
            if MAX < graph[i][j]:
                MAX = graph[i][j]
    
    return MAX-1


bfs()

print(result(graph))
