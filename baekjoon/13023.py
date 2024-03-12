def dfs(now, cnt):
    global result
    if cnt == 5:
        result = 1
        return result

    for ne in graph[now]:
        
        if not visited[ne]:
            visited[ne]  = 1
            dfs(ne,cnt + 1)
            visited[ne]  = 0

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
visited = [0] * n
result = 0


for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(n):
    visited[i] = 1
    dfs(i,1)
    visited[i] = 0

print(result)