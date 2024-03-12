from collections import deque
def topology_sort():
    global result
    result = []
    q = deque()


    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    

    while q:
        now = q.popleft()
        result.append(now)

        for i in height[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)



n,m = map(int,input().split())
indegree = [0] * (n+1)
height = [[] for _ in range(n+1)]
result = []
for _ in range(m):
    a,b = map(int,input().split())
    height[a].append(b)
    indegree[b] +=1

topology_sort()
print(*result)