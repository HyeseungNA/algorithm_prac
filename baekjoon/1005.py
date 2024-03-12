def acm():
    q = deque()
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            dp[i] = cost[i]
            q.append(i)
    while q:
        from_node = q.popleft()
        for to_node in graph[from_node]:
            indegree[to_node] -= 1
            dp[to_node] = max(dp[to_node], cost[to_node] + dp[from_node])
            if indegree[to_node] == 0:
                q.append(to_node)

    if indegree[end] == 0:
        print(dp[end])


from collections import deque

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    cost = [0] + list(map(int,input().split()))
    dp = [0] * (n+1)
    indegree = [0] * (n+1)
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        indegree[b] += 1
    end = int(input())
    acm()