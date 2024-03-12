def dfs(y, x, cnt, total):
    global Max
    if cnt == 4:
        Max = max(total, Max)
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            dfs(ny, nx, cnt + 1, total + Map[ny][nx])
            visited[ny][nx] = 0

def fu(y, x):
    global Max
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    tmp = []

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m:
            tmp.append(Map[ny][nx])

    if len(tmp) == 4:
        tmp.sort(reverse=True)
        tmp.pop()
        Max = max(Max, sum(tmp) + Map[y][x])

    elif len(tmp) == 3:
        Max = max(Max, sum(tmp) + Map[y][x])

    visited[y][x] = 0  # 방문 처리 제거

n, m = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
Max = int(-12e9)
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, Map[i][j])
        fu(i, j)
        visited[i][j] = 0
print(Max)
