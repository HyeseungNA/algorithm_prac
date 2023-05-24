def dfs1(y,x):
    global cnt1
    cnt1 += 1

    dy = [-1,0,1,0]
    dx = [0,-1,0,1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<= nx < n and 0<= ny < m and visited1[ny][nx] == 0 and army[ny][nx] == 'W':
            visited1[ny][nx] = 1
            dfs1(ny,nx)
        


def dfs2(y,x):
    global cnt2
    cnt2 += 1

    dy = [-1,0,1,0]
    dx = [0,-1,0,1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<= nx < n and 0<= ny < m and visited2[ny][nx] == 0 and army[ny][nx] == 'B':
            visited2[ny][nx] = 1
            dfs2(ny,nx)


n,m = map(int,input().split())

army = [list(input()) for _ in range(m)]

visited1 = [[0] * n for _ in range(m)]
visited2 = [[0] * n for _ in range(m)]

#'W'병사 DFS
total1 = 0
cnt1= 0 
for i in range(m):
    for j in range(n):
        if army[i][j] == 'W' and visited1[i][j] == 0:
            visited1[i][j] = 1
            dfs1(i,j)
            total1 += cnt1 ** 2
            cnt1= 0 

#'B'병사 DFS
total2 = 0
cnt2 = 0
for i in range(m):
    for j in range(n):
        if army[i][j] == 'B' and visited2[i][j] == 0:
            visited2[i][j] = 1
            dfs2(i,j)
            total2 += cnt2 ** 2
            cnt2= 0 

print(total1,total2)