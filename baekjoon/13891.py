n, m = map(int,input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]
result = []
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0
        

for i in range(1, n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(1,n+1):
    total = 0
    for j in range(1,n+1):
        if graph[i][j] == INF:
            continue
        total += graph[i][j]
    
    result.append(total)

Min = int(1e9)
idx = 0
for i in range(n):
    if Min > result[i]:
        Min = result[i]
        idx = i
print(idx+1)