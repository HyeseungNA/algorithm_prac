from collections import deque

def bfs(y,x,size,cnt,sec):# y좌표, x좌표, 사이즈, 먹은 횟수, 이동 시간
    global time
    q.append([y,x,size,cnt,sec])


    while q:
        y,x,size,cnt,sec = q.popleft()
        # print(y,x,size,cnt,sec) # 현재 y위치, x위치, 사이즈, 먹은 갯수, 이동거리
        time += sec
        if cnt == size:
            size += 1 # 해당 크기만큼 먹어치웠으면 사이즈 키워줘,,
            cnt = 0 # 사이즈 키우기 위해 먹어야 하는 물고기 수 초기화

        tmp = [] # 먹을 수 있는 먹이들 위치
        # 사이즈가 작은 물고기들 리스트에 넣어주기
        for i in range(n):
            for j in range(n):
                if 0 < oceans[i][j] < size:
                    tmp.append([i,j]) # 먹이 y좌표, x좌표, 먹으면 커지는 사이즈, 거리
        

        dy = [-1,0,1,0]
        dx = [0,-1,0,1]
        possible = []
        for t in tmp:
            q2 = deque()
            q2.append([y,x,0]) # 현재 상어 y좌표, 현재 상어 x좌표, 거리
            ty = t[0] # 도착지점
            tx = t[1] # 도착지점
            visited = [[0] * n for _ in range(n)]
            visited[y][x] = 1

            while q2:
                now_y,now_x,dis = q2.popleft()
                if now_y == ty and now_x == tx: # 해당 위치 도착했으면
                    possible.append([dis,ty,tx])
                    break

                for i in range(4):
                    ny = now_y + dy[i]
                    nx = now_x + dx[i]

                    if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0:
                        if oceans[ny][nx] <= size or oceans[ny][nx] == oceans[ty][tx]:
                            visited[ny][nx] = 1
                            q2.append([ny,nx,dis+1])
                        


        possible.sort(key=lambda x:(x[0],x[1],x[2])) # 걸린 시간, 물고기 y좌표, 물고기 x좌표
        if possible:
            now = possible[0]
            new_sec, new_y,new_x = now[0], now[1], now[2]
            oceans[new_y][new_x] = 0 

            q.append([new_y, new_x, size, cnt + 1, new_sec])






n = int(input())
oceans = [list(map(int,input().split())) for _ in range(n)]
q = deque()
time = 0
for i in range(n):
    for j in range(n):
        if oceans[i][j] == 9:
            oceans[i][j] = 0
            bfs(i,j,2,0,0) # y좌표, x좌표, 사이즈, 먹은 횟수, 이동 시간

print(time)