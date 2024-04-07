from collections import deque

def bfs(y,x):
    q = deque()
    q.append([y,x])

    while q:
        y,x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < n and 0 <= nx < m and ices[ny][nx] != 0 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append([ny,nx])


def melt():

    for i in range(len(tmp)):
        cnt = 0
        y = tmp[i][0]
        x = tmp[i][1]

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < n and 0 <= nx < m and ices[ny][nx] == 0:
                cnt += 1
        
        tmp[i].append(cnt)


    for y,x,cnt in tmp:
        if ices[y][x] - cnt < 0:
            ices[y][x] = 0

        else:
            ices[y][x] = ices[y][x] - cnt          
    return

n,m = map(int,input().split())
ices = [list(map(int,input().split())) for _ in range(n)]
dy = [-1,0,1,0]
dx = [0,-1,0,1]
answer = 0
while True:
    tmp = []
    for i in range(n):
        for j in range(m):
            if ices[i][j] != 0:
                tmp.append([i,j])
    
    if tmp: # 빙하가 있다면
        melt() # 녹여주기
        visited = [[0]* m for _ in range(n)]
        frag = 0 # 덩어리
        
        for i in range(n): 
            for j in range(m):
                if ices[i][j] != 0 and visited[i][j] == 0:
                    visited[i][j] = 1
                    frag += 1
                    bfs(i,j) 
        
        answer += 1
        # for v in visited:
        #     print(v)
        # print('++++++++++')
        if frag >= 2:
            print(answer)
            exit()
    else:
        print(0)
        break





'''

5 5
0 0 0 0 0
0 1 1 1 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0

0


4 4
0 0 0 0
0 3 1 0
0 1 3 0
0 0 0 0

1

5 7
0 0 0 0 0 0 0
0 3 3 2 3 3 0
0 4 0 4 0 3 0
0 0 0 0 4 3 0
0 0 0 0 0 0 0

0

'''