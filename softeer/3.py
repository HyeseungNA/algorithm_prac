# 가다가 1을 만나면 멈춰버리기
# 이어진 0이 2개 이상이면 q에 넣어주기


import deque
def check(y,x):
    cnt = 0
    dy = [-1,0,1,0]
    dx = [0,-1,0,1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx <m:
            # 외부 공기를 만나면 개수 더해주기
            if ice[ny][nx] == 0:
                cnt +=1
            # 얼음을 만나버리면 끝내주기
            else:
                break
    # 외부공기가 2이상이면 True return 
    if cnt >= 2:
        return True
    else:
        return False




n,m = map(int,input().split())
ice = [list(map(int,input().split())) for _ in range(n)]

q = deque()


#  외부 공간이 2개 이상인지 확인하기
for i in range(n):
    for j in range(m):
        if ice[i][j] == 1:
            y = i
            x = j
            # 두 개 이상이면 bfs 시작
            if check(i,j):
                bfs(i,j)
