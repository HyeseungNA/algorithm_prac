import sys
sys.setrecursionlimit(10**6)
def dfs(y,x):

    #다음 노드 찾기
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        #현재 값이 범위 안에 있고 방문을 안하고 현재 값이랑 다음 값이 같으면 다음 노드로 가기
        if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and  (graph[ny][nx] == graph[y][x]):
            visited[ny][nx] = 1
            dfs(ny,nx)


n= int(input())
graph = []

#구역 수 
cnt1 = 0
cnt2 = 0
visited = [[0]*n for _ in range(n)]

for _ in range(n):
    graph.append(list(input()))
print(graph)

#정상인
for y in range(n):
    for x in range(n):
        #방문을 안한 지점 dfs 시작
        if visited[y][x] == 0:
            visited[y][x] = 1
            cnt1 += 1
            dfs(y,x)


#적록색약
for y in range(n):
    for x in range(n):
        #빨간색을 녹색으로 바꿔주기
        if graph[y][x] == "R":
            graph[y][x] = 'G'


visited = [[0]*n for _ in range(n)]


for y in range(n):
    for x in range(n):
        #방문안하면 dfs 시작
        if visited[y][x] == 0:
            visited[y][x] = 1
            cnt2 += 1
            dfs(y,x)

print(cnt1,cnt2)

'''
3
GRR
BRR
GBR
'''