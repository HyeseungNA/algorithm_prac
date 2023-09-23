from collections import deque
# 빨간공 파란 공 이동
def move(x, y, dx, dy):
    cnt = 0

    while boards[y + dy][x + dx] != '#' and boards[y][x] != 'O':
        x += dx
        y += dy
        cnt += 1
    return y, x, cnt


    
def go():
    global Min
    
    # 큐가 없을 때까지 계속
    while q:
        # 현재 위치와 이동횟수
        ry,rx,by,bx,total = q.popleft()
        if total > 10:
            break

        # 사방탐색 시작
        for i in range(4):
            rny, rnx, r_cnt = move(rx,ry,dx[i],dy[i])
            bny, bnx, b_cnt = move(bx,by,dx[i],dy[i])

            # 파란 공이 구멍안에 안들어가면
            if boards[bny][bnx] != 'O':
                if rny == bny and rnx == bnx:

                    # 빨간공이 구멍에 들어가면
                    if boards[rny][rnx] == 'O':
                        if Min > total:
                            Min = total

                    # 빨간공 횟수가 더 크면
                    if r_cnt > b_cnt:
                        rny -= dy[i]
                        rnx -= dx[i]
                    else:
                        bny -= dy[i]
                        bnx -= dx[i]

                if visited[rny][rnx] == 0 and visited[bny][bnx] == 0:
                    visited[rny][rnx] = 1
                    visited[bny][bnx]  = 1
                    q.append((ry,rx,by,bx,total+ 1))
     
    return Min




n,m = map(int,input().split())
boards = [list(input()) for _ in range(n)]
ry = 0
rx = 0
by = 0
bx = 0
Min = 11
# 사방탐색 방향
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


# 빨간공, 파란공 위치 파악하기
for i in range(n):
    for j in range(m):
        if boards[i][j] == 'R':
            ry = i
            rx = j
        
        elif boards[i][j] == 'B':
            by = i
            bx = j

# 빨간 공 현재 위치, 이동횟수 큐에 넣어주기
q = deque()
q.append((ry,rx,by,bx,1))
visited = [[0] * m for _ in range(n)]
go()

if Min > 10:
    print(-1)
else:
    print(Min)
