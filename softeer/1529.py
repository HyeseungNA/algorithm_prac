
import sys
sys.setrecursionlimit(10**6)
def dfs(now,adj,visited):
    if visited[now] == 1:
        return
    
    visited[now] = 1

    for point in adj[now]:
        dfs(point,adj,visited)

n,m = map(int,input().split())
adj = [[]  for _ in range(n+1)]
adjR = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    adj[x].append(y)
    adjR[y].append(x)

start,end = map(int,input().split())
towork = [0] * (n + 1)
towork[end] = 1
dfs(start,adj,towork)

tohome = [0] * (n + 1)
tohome[start] = 1
dfs(end,adj,tohome)


fromWork = [0] * (n + 1)
fromHome = [0] * (n + 1)

dfs(end,adjR,fromWork)
dfs(start,adjR,fromHome)
'''
5 9
1 2
1 4
2 1
2 3
3 4
3 5
4 1
4 3
5 1
1 3

'''
cnt = 0
for i in range(1,n+1):
    if fromHome[i] and fromWork[i] and tohome[i] and towork[i]:
        cnt += 1

print(cnt - 2)