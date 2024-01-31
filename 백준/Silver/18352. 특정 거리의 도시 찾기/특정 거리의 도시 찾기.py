from collections import deque
def bfs(now):
    q = deque()
    q.append([now,0])
    
    while q:
        now,cnt = q.popleft()
        if cnt == k:
            result.append(now)
        for ne in graph[now]:
            if visited[ne] == 0:
                visited[ne] = 1
                q.append([ne,cnt+1])


n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
result = []
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
# print(graph)
visited[x] = 1
bfs(x)
result.sort()
if not result:
    print(-1)
else:
    for el in result:
        print(el)

'''
4 4 2 1
1 2
1 3
3 4
2 1
'''