from collections import deque

def bfs(y, x):
    q = deque()
    q.append([y, x])
    cnt = 0

    while q:
        y, x = q.popleft()
        
        cnt += 1
        dy = [-1, 0, 1, 0]
        dx = [0, -1, 0, 1]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and pictures[ny][nx] == 1:
                visited[ny][nx] = 1
                q.append([ny, nx])


    return cnt

n, m = map(int, input().split())
pictures = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result = []

for i in range(n):
    for j in range(m):
        if pictures[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            result.append(bfs(i, j))


if not result:
    print(0)
    print(0)
else:
    print(len(result))
    print(max(result))