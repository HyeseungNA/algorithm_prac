import sys
sys.setrecursionlimit(10000)


def dfs(y,x):
    global farm
    # 지렁이가 이동 못하게 만들어주기
    farm[y][x] = 2


    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 범위 안에 있고 다음에 갈 곳에 배추가 심어져 있다면 지렁이 이동해라

        if  0 <= nx < M and 0 <= ny < N and farm[ny][nx] == 1:
            dfs(ny,nx)
            


T = int(input())
for _ in range(T):
    cnt = 0
    M,N,K  = map(int,input().split()) #가로길이, 세로길이, 배추 개수
    farm = [[0]*M for _ in range(N)]


    for _ in range(K):
        X,Y = map(int,input().split()) # 배추 위치
        farm[Y][X] = 1 # 배추 넣어주기


    # 배추가 심어져 있으면 dfs
    for y in range(N):
        for x in range(M):
            if farm[y][x] == 1:
                dfs(y,x)
                cnt += 1
    print(cnt)
  



        
