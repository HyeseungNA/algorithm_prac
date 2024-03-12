import itertools,copy
from collections import deque

def bfs(y,x):
    q = deque()
    q.append([y,x])

    while q:
        y,x = q.popleft()

        dy = [-1,0,1,0]
        dx = [0,-1,0,1]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if Map2[ny][nx] == 0:
                    Map2[ny][nx] = 2
                    q.append([ny,nx])

    return


n,m = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(n)]
tmp = []
for i in range(n):
    for j in range(m):
        if Map[i][j] == 0:
            tmp.append([i,j])



walls = list(itertools.combinations(tmp,3))

Max = int(-1e9)
for wall in walls:
    cnt = 0
    Map2 = copy.deepcopy(Map)
    for i,j in wall:
        Map2[i][j] = 1 # 벽으로 만들어준다. 

    for y in range(n):
        for x in range(m):
            if Map2[y][x] == 2:
                bfs(y,x)
    for y in range(n):
        for x in range(m):
            if Map2[y][x] == 0:
                cnt += 1
    
    # print(Map2)
    # print('----------------')
    Max = max(cnt,Max)

print(Max)