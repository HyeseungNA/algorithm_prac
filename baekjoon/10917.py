import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)
def dfs(st,now,cnt,total):
    global Min
    if total > Min:
        return
    
    if cnt == n and st == now:
 
        Min = min(Min,total)
        return
    for i in range(n):
        if visited[i] == 0 and costs[now][i] != 0:
            visited[i] = 1
            # lst.append([now,i,costs[now][i]])
            dfs(st,i,cnt +1,total + costs[now][i])
            visited[i] = 0
            # lst.pop()


n = int(input())
costs = [list(map(int,input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
lst = []
visited = [0] * n
Min = int(12e9)

for i in range(n):
    dfs(i,i,0,0)

print(Min)