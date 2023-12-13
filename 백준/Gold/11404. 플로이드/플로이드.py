n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]


for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(c, graph[a][b])


# 자기자신 초화
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for i in range(1, n+1): # i는 노드
    for j in range(1, n+1): # j는 출발지
        for k in range(1, n+1): # k는 도착지
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(1,n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0,end = ' ')
        else:
            print(graph[i][j], end = ' ')
    print()