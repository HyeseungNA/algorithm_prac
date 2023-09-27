# cctv 탐색 
# 사방탐색하고 채워넣기
import sys,copy
input = sys.stdin.readline

def fill(tmp,i,y,x):

    # 감시 영역 채우기 
    for d in range(i):

        while True:
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 > ny or ny >= n or 0 > nx or nx >= m:
                break

            if tmp[ny][nx] == 6:
                break
            if tmp[ny][nx] == 0:
                tmp[ny][nx] = 9


    return





def dfs(dept,graph):
    global Min
    if dept == len(cctv):

        # 0의 개수 return
        cnt = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    cnt += 1
        
        if cnt < Min:
            Min = cnt
    return Min

    # 배열 복사
    tmp = copy.deepcopy(graph)
    num,y,x = cctv[dept]
    for i in range(num):
        fill(tmp,i,y,x)
        dfs(dept+1,tmp)
    



n,m = map(int,input().split())
cctv = []
graph = []
Min = int(1e9)
# 상, 우, 하, 좌
dy = [-1,0,1,0]
dx = [0,-1,0,1]

order = [
    [],
    [0,1,2,3],
    [[0,2],[1,3],[2,4]],
    [[0,1,2],[1,2,3],[0,1,3]],
    [[0,1,2,3]]
]


for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if graph[i][j] in [1,2,3,4,5]:
            # cctv번호, y좌표, x좌표 담아주기
            cctv.append([graph[i][j],i,j])

print(dfs(0,graph))