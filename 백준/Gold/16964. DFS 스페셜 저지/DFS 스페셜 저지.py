from collections import deque

def dfs(cur):
    global visited, result, graph
    
    visited[cur] = True
    set_ = set()
    for next_ in graph[cur]:
        if visited[next_] == 0:
            set_.add(next_)
    
    while set_:
        temp = result.popleft()
        if temp in set_:
            set_.remove(temp)
            dfs(temp)
        else:
            return False
    
    return True

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
result = deque(map(int, input().split()))
visited = [False] * (N + 1)



first = result.popleft()
if first != 1:
    print("0")
else:
    if dfs(1):
        print("1")
    else:
        print("0")
