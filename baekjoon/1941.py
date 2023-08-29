def dfs(y,x,cnt):
    global total
    
    # cnt 가 7이면 돌아가기
    if cnt == 7:
        print(visited)
        print(answer)
        # 이다솜파 사람들이 4명이상이면 더해주기
        if answer.count('S') >= 4:
            # print(visited)
            # print(answer)
            print('888888888888888888')
            total += 1
        return
    
    # 가로, 세로 인접 확인
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 범위 확인, 방문 확인
        if 0 <= ny < 5 and 0 <= nx < 5 and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            answer.append(girls[ny][nx])
            dfs(ny,nx,cnt + 1)
            visited[ny][nx] = 0
            answer.pop()
                
                    

girls = [list(input()) for _ in range(5)]
answer = [] # 칠공주 넣을 리스트
visited = [[0] * 5 for _ in range(5)]
total = 0
for i in range(5):
    for j in range(5):
        # 방문 안했으면 dfs 들어가기
        if visited[i][j] == 0:
            answer.append(girls[i][j])
            visited[i][j] = 1
            dfs(i,j,1) # x좌표, y좌표 , 깊이
            if i==1 and j==0:
            print('----------------')
            answer.pop()
print(total)