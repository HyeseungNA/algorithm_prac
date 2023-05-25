from collections import deque

def bfs(y,x):
    global cnt

    q.append([y,x])

    while q:
        cnt += 1
        y,x=  q.popleft()
        

        dy = [-1,0,1,0]
        dx = [0,-1,0,1]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0 <= nx < n and home[ny][nx] == 1:
                home[ny][nx] = 2
                q.append([ny,nx])

n= int(input())
home = [list(map(int,input())) for _ in range(n)]
cnt_list = []
result = 0
q = deque()
for i in range(n):
    for j in range(n):
        if home[i][j] == 1:
            cnt = 0
            home[i][j] = 2
            bfs(i,j)
            result += 1
            cnt_list.append(cnt)
print(result)
cnt_list.sort()
for c in cnt_list:
    print(c)

        