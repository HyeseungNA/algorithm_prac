from collections import deque

def dfs(now):
    global visited, plan, graph
    
    visited[now] = True # 방문처리 해주기

    possible = set() # 매번 초기화 
    for ne in graph[now]: # 다음 지점으로 갈 수 있는 곳들 중에서
        if visited[ne] == 0: # 방문할 수 있으면
            possible.add(ne) # 갈 수 있는 곳(set)에 추가 하기
    
    while possible: #갈 수 있는 곳들이 남아 있을 때까지
        temp = plan.popleft() # 그 다음으로 계획한 곳이
        if temp in possible: # 갈 수 있는 곳에 들어 있다면
            possible.remove(temp) # 갈 수 있는 곳(set)에서 없애주기
            dfs(temp)
        else:
            return False # 갈 수 있는 곳(set)에 없다면 계획이 잘 못 되었으니 false
            
    return True # 이 부분 중요,,이 부분 빼서 꽤나 헤맸던,,,

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a,b = map(int, input().split())
    graph[a].append(b) 
    graph[b].append(a)
plan = deque(map(int, input().split()))
visited = [False] * (n + 1)

first = plan.popleft()
if first != 1:
    print("0")
else:
    if dfs(1):
        print("1")
    else:
        print("0")
