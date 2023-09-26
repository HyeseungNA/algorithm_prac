from collections import deque

n,m = map(int,input().split())
y,x,d = map(int,input().split())
places = [list(map(int,input().split())) for _ in range(n)]
cnt = 1


# 북, 동 남, 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 청소 표시
places[y][x] = 2

while True:
    # 아직 청소 안함
    flag = 0
    # 사방 탐색
    for _ in range(4):
        d = (d + 3) % 4

        ny = y + dy[d]
        nx = x + dx[d]

        # 만약에 현재 청소를 했으면 멈춰
        if 0 <= ny < n and 0 <= nx < m:
            # 아직 청소가 안되어 있으면
            if places[ny][nx] == 0:
                # 청소하고
                places[ny][nx] = 2
                # 이동
                y = ny
                x = nx
                # 이동 
                cnt += 1
                flag = 1
                break
    
    if flag == 0:
        if places[y-dy[d]][x-dx[d]] == 1:
            print(cnt)
            break
        else:
            y -= dy[d]
            x -= dx[d]

    






