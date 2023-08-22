def dfs(now, cnt):
    global lst
    # 현재 값 넣어주기
    lst.append(now)
    # 방문 처리해주def dfs(now, cnt):
    global lst
    # 현재 값 넣어주기
    lst.append(now)
    # 방문 처리해주기
    visited[now] = 1
    # 만약에 깊이가 n이면 lst 출력
    if cnt == n:
        print(*lst)
        return

    for i in range(1,n+1):
        if visited[i] == 0:
            dfs(i,cnt + 1)
            # 다시 방문할 수 있게 만들어주기
            visited[i] = 0
            lst.pop()

n = int(input())
# 방문 배열
visited = [0] * (n + 1)
lst = []
for i in range(1,n+1):
    # 방문을 안했으면 dfs
    if visited[i] == 0:
        dfs(i,1) # 현재 값, cnt
        visited[i] = 0
        lst.pop()
    visited[now] = 1
    # 만약에 깊이가 n이면 lst 출력
    if cnt == n:
        print(*lst)
        return

    for i in range(1,n+1):
        if visited[i] == 0:
            dfs(i,cnt + 1)
            # 다시 방문할 수 있게 만들어주기
            visited[i] = 0
            lst.pop()

n = int(input())
# 방문 배열
visited = [0] * (n + 1)
lst = []
for i in range(1,n+1):
    # 방문을 안했으면 dfs
    if visited[i] == 0:
        dfs(i,1) # 현재 값, cnt
        visited[i] = 0
        lst.pop()