n, m = map(int,input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
result = 0
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1




for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1



for i in range(1,n+1):
    answer = 0
    for j in range(1,n+1):
        answer += graph[i][j] + graph[j][i]
    if answer == n-1:
        result += 1

print(result)