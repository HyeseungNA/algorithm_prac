
from collections import deque
def dfs(now):
    print(now,end = ' ')
    visited[now] = 1


    for i in adj[now]:
        if visited[i] == 0:
            dfs(i)


def bfs(now):
    q = deque()
    q.append(now)
    visited2[now] = 1

    while q:
        point = q.popleft()
        print(point,end = ' ')
        for i in adj[point]:
            if visited2[i] == 0:
             q.append(i)
             visited2[i] = 1

        



N,M,V = map(int,input().split())
adj = [[] for _ in range(N+1)]

visited = [0] * (N+1)
visited2 = [0] * (N+1)
for _ in range(M):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

for _ in range(N+1):
    adj.sort()
#dfs
dfs(V)

print()
#bfs
bfs(V)
