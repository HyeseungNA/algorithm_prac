from collections import deque

#현재위치,바이러스 걸린 갯수
def bfs(v):
    cnt = 0
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        point= q.popleft()
        for i in adj[point]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = 1
                q.append(i)
    return cnt






computers = int(input())
n = int(input())
adj = [[] for _ in range(computers+1)]
visited = [0] * (computers+1)
for _ in range(n):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)


print(bfs(1))

