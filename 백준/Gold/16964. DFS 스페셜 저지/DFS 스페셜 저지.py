from collections import deque
def dfs(plan):

    now = plan.popleft()
    visited[now] = 1
    if not plan:
        print(1)
        exit()
    
    for _ in graph[now]:
        if plan[0] in graph[now] and visited[plan[0]] == 0:
            dfs(plan)
    

n = int(input())
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

plan = deque(list(map(int,input().split())))


if plan[0] != 1:
    print(0)
else:
    dfs(plan)
    print(0)