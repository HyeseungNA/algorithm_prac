def dfs(y,x,cnt):
    global total
    
    # cnt 가 7이면 돌아가기
    if cnt == 7:
        # 이다솜파 사람들이 4명이상이면 더해주기
        if answer.count('S') >= 4:
            print(visited)
            print(answer)
            total += 1
        return
    
    for ny in range(5):
        for nx in range(5):
            # 방문을 확인하고
            if visited[ny][nx] == 0:
                # 가로 세로에 인접해 있는지 확인
                dy = [-1,0]
                dx = [0,-1]

                for m in range(2):
                    py = ny + dy[m]
                    px = nx + dx[m]

                    if visited[py][px] == 0:
                        answer.append(girls[ny][nx])
                        visited[ny][nx] = 1
                        dfs(ny,nx, cnt + 1)
                        answer.pop()
                        visited[ny][nx] = 0


girls = [list(input()) for _ in range(5)]
answer = [] # 칠공주 넣을 리스트
visited = [[0] * 5 for _ in range(5)]
total = 0
for i in range(5):
    for j in range(5):
        # 방문 안했으면 하기
        if visited[i][j] == 0:
            answer.append(girls[i][j])
            visited[i][j] = 1
            dfs(i,j,1) # x좌표, y좌표 , 깊이
            answer.pop()
            visited[i][j]  = 0
