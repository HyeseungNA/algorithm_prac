from collections import deque
def bfs(now):
    global result
    q = deque()
    q.append([now,0])
    cnt = 0
    while q:
        now,cnt = q.popleft()
        if now == c:
            result = cnt
            break
            

        for num in graph[now]:
            if visited[num] == 0:
                visited[num] = 1
                q.append([num,cnt+1])
    return

n = int(input())
p,c = map(int,input().split())
k = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
result = -1
for _ in range(k):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[p] = 1
bfs(p)
print(result)