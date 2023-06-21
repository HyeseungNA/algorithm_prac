from collections import deque

# 내부 공기 표시해주기
def check(y,x):
    inner = [[0]  * m for _ in range(n)]

    # 모든 방향을 탐색
    dy = [-1,0,1,0]
    dx = [0,-1,0,1]
    for i in range(4):
        idx = 1
        cnt = 0
        while True:
            ny = y + (dy * idx)
            nx = x + (dx * idx)
            # 범위를 벗어날때까지 긔
            if 0 > ny or ny > n or 0 > nx or nx > m:
                break
            # 만약에 가다가 얼음을 만나면 개수 추가
            if inner[ny][nx] == 1:
                cnt += 1
            # 만난 얼음이 4개라면 내부 얼음 표시 해주기
            if cnt == 4:
                inner[y][x] = 2
            idx += 1





def bfs(y,x):
    # 외부 공기가 2개 이상이면 q에 넣어주기
    
    while q:


    dy = [-1,0,1,0]
    dx = [0,-1,0,1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= nx < m and 0 <= ny < n:
            if ice[ny][nx] == 0:
                cnt += 1
    

    if cnt >= 2:
        q.append(ny,nx)
    


n,m = map(int,input().split())
ice = [list(map(int,input().split())) for _ in range(n)]
q = deque()


for i in range(m):
    for j in range(n):
        check(i,j)

for i in range(m):
    for j in range(n):
        if ice[i][j] == 1:
            bfs(i,j)

