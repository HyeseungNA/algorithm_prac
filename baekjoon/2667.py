import sys
sys.setrecursionlimit(2500)
def dfs(y,x):
    global cnt
    cnt += 1 # 단지를 칠할 때마다 cnt를 더해준다. 
    dy = [-1,0,1,0]
    dx = [0,-1,0,1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 범위 내에 있고 방문을 안했으면 dfs 시작
        if 0 <= nx < n and 0 <= ny < n and home[ny][nx] == 1:
            home[ny][nx] = 2
            dfs(ny,nx)


n= int(input())
home = [list(map(int,input())) for _ in range(n)]
result = 0 # 총 단지 수
cnt_list = []
for i in range(n):
    for j in range(n):
        # 1일 때 dfs 시작
        if home[i][j] == 1:
            home[i][j] = 2
            cnt = 0
            dfs(i,j)
            result += 1
            cnt_list.append(cnt)


print(result)
cnt_list.sort()
for c in cnt_list:
    print(c)
