import copy

n, m = map(int, input().split())
cctv = []
graph = []

# 북 - 동 - 남 - 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])

def fill(board, y, x, direction):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                break
            if board[ny][nx] == 6:
                break
            elif board[ny][nx] == 0:
                board[ny][nx] = 7

def dfs(depth, arr):
    global min_value

    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        min_value = min(min_value, count)
        return
    cctv_num, y, x = cctv[depth]
    for direction in mode[cctv_num]:
        temp = copy.deepcopy(arr)
        fill(temp, y, x, direction)
        dfs(depth + 1, temp)

min_value = int(1e9)
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

dfs(0, graph)
print(min_value)
