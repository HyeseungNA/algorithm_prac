n,m,r = map(int,input().split())
items = [0] + list(map(int,input().split()))
INF = int(21e8)
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(r):
    a,b,distance = map(int,input().split())
    graph[a][b] = distance
    graph[b][a] = distance

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][k] + graph[k][b] , graph[a][b])
Max = 0

for i in range(n+1):
    result = items[i]
    for j in range(n+1):
        if i != j:
            if graph[i][j] <= m:
                result += items[j]
    Max = max(result,Max)

print(Max)
