# 모든 경우의 수를 다 보기,,?
# R의 이동 관련한 방문 리스트 만들기


def check(y,x,d):
    cnt = 0
    # 다음 갈 곳이 범위 안에 있으면
    ny = y + dy[d]
    nx = x + dx[d]
    while True:
        if 0 <= ny < n and 0 <= nx < m:
            if boards[ny][nx] != '#' or boards[y][x] != '0':
                y = ny
                x = nx
                cnt += 1

    return y,x,cnt

    # 이동

def go(rx,ry,bx,by,cnt):

    if cnt > 10 :
        return
    # 빨간공이 0을 만나면 멈춰
    if boards[ry][rx] == 'O':
        result.append(cnt)
        return

    # 사방탐색 시작
    for i in range(4):
        rny,rnx,rcnt = check(ry,rx,i)
        bny,bnx,bcnt = check(by,bx,i)

        # 만약에 파란공이 먼저 구멍에 들어가면
        # 다시 해야됨
        if boards[bny][bnx] == 'O':
            return 

        # 만약에 둘다 같은 곳이면?
        # 더 빨리 도착한 공한테 양보하세요
        if rny == bny and rnx == bnx:
            if rcnt > bcnt:
                rny -= dy[i]
                rnx -= dx[i]
            else:
                bny -= dy[i]
                bnx -= dx[i]
            
        # 빨간 공이 구멍이면?
        if boards[bny][bnx] == 'O':
            Min = min(Min,cnt)
    go(rx,ry,bx,by,cnt+1)
        

n,m = map(int,input().split())
boards = [list(input()) for _ in range(n)]
v1 = [[0] * m for _ in range(n)]
# 상하좌우 보기
dy = [-1,1,0,0]
dx = [0,0,-1,1]
Min = 11
rx= 0
ry = 0
bx = 0
by = 0
# 빨간 공 위치 파악, 파란 공 위치 파악
for i in range(n):
    for j in range(m):
        if boards[i][j] == 'R':
            rx = j
            ry = i
        if boards[i][j] == 'B':
            bx = j
            by = i
            go(rx,ry,bx,by,1)

print(min(result))