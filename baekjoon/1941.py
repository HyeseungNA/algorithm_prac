from collections import deque

def bfs(y,x):
    v2 = [[0] * 5 for _ in range(5)]
    q = deque()
    q.append((y,x))
    v2[y][x] = 1
    cnt = 1

    while q:
        y,x = q.popleft()
        dy = [-1,0,1,0]
        dx = [0,-1,0,1]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < 5 and 0 <= nx < 5 and v1[ny][nx] == 1 and v2[ny][nx] == 0:
                q.append((ny,nx))
                cnt += 1

    if cnt == 7:
        return True

def check():
    for i in range(5):
        for j in range(5):
            if v1[i][j] == 1:
                return bfs(i,j)



def dfs(n,cnt,scnt):
    global total
    if cnt == 7:
        print(v1)
        if scnt >= 4:
            if check():
                total += 1

        return
    v1[n//5][n%5] = 1
    dfs(n+1,cnt+1,scnt+int(girls[n//5][n%5] == 'S'))
    v1[n//5][n%5] = 0
    dfs(n+1,cnt+1,scnt)


girls = [list(input()) for _ in range(5)]
v1 = [[0] * 5 for _ in range(5)]
total = 0
dfs(0,0,0) # 사람 인덱스, 깊이, 다솜파 수
print(total)