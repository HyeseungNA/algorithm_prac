            
from collections import deque

def dfs(v):
    print(v,end =' ')
    visited[v] = 1
    
    for i in adj[v]:
        if visited[i] == 0:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visited2[v] = 1
    while q:
        point = q.popleft()
        print(point,end = ' ')
        for i in adj[point]:
            if visited2[i] == 0:
                q.append(i)
                visited2[i] = 1


#입력
n,m,start = map(int,input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    line = list(map(int, input().split()))
    adj[line[0]].append(line[1])
    adj[line[1]].append(line[0])
for i in range(n+1):
    adj[i].sort()
visited = [0] * (n+1)
visited2 = [0] * (n+1)
#DFS
dfs(start)
print()
#BFS
bfs(start)





