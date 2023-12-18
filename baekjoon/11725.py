import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(now):
    visited[now] = 1

    for i in result[now]:
        if visited[i] == 0:
            parent[i] = now
            dfs(i)

n = int(input())
result = [[] for _ in range(n+1)]
visited = [0] * (n+1)
parent = [0] * (n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    result[a].append(b)
    result[b].append(a)


dfs(1)

for i in range(2,n+1):
    print(parent[i])