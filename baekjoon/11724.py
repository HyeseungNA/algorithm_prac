from collections import deque

def bfs(now):
    
    while q:
        now = q.popleft()

        for i in range(n+1):
            if adj[now][i] == 1 and v[i] == 0:
                v[i] = 1
                q.append(i)

n,m = map(int,input().split())
adj = [[0] * (n+1) for _ in range(n+1)]
v = [0] * (n+1)
cnt = 0
q = deque()
for _ in range(m):
    a,b = map(int,input().split())
    adj[a][b] = 1
    adj[b][a] = 1



for i in range(1, n+1):
    if v[i] == 0:
        q.append(i)
        v[i] = 1
        cnt += 1
        bfs(i)
       
print(cnt)