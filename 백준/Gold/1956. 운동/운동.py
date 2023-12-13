n, m = map(int,input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]
Min = int(1e9)
result = []
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c




for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k] = min(graph[j][k] , graph[j][i] + graph[i][k])

Min = int(1e9)
for i in range(1,n+1):
    if Min > graph[i][i]:
        Min = graph[i][i]
    
if Min == INF:
    print(-1)
else:
    print(Min)