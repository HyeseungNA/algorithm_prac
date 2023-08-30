# 7개를 찾다
# 다솜이 우위에 있는지
# 인접하는지

from collections import deque
import copy
def check():
    q = deque()
    v2 = copy.deepcopy(v1)

    dy = [-1,0,1,0]
    dx = [0,-1,0,1]

    while q:
        y,x = q.popleft()

        for m in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and v2[ny][nx] == 0:
                v2[ny][nx] = 1
                q.append((ny,nx,cnt+1))
    # 방문 안한것을 q안에 넣기
    for i in range(5):
        for j in range(5):
            if v2[i][j] == 0:
                v2[i][j] = 1
                q.append((i,j,cnt))

    if cnt == 7:
        return True
    return
    


def dfs(lst,cnt):

    # cnt가 7이면 return 
    if cnt == 7:
        # 다솜이 우위에 있는 판별
        if lst.count('S') >= 4:
            if check():
                total += 1
            print(lst)
        return


    for i in range(5):
        for j in range(5):
            if v1[i][j] == 0:
                lst.append(girls[i][j])
                v1[i][j] = 1
                dfs(lst,cnt + 1)
                lst.pop()
                v1[i][j] = 0
                dfs(lst,cnt)



girls = list(input() for _ in range(5))
v1 = [[0] * 5 for _ in range(5)]
total = 0
# 7개를 찾다
for i in range(5):
    for j in range(5):
        lst = [] # 칠공주 넣을 곳
        # 방문 안하면 dfs
        if v1[i][j] == 0:
            v1[i][j] = 1
            lst.append(girls[i][j])
            dfs(lst,1)

print(total)