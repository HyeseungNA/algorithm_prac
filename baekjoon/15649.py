def dfs(now,cnt):
    if cnt == m:
        print(*result)
        return
    
    for i in range(1,n+1):
        if visited[i] == 0:
            visited[i] = 1
            result.append(i)
            dfs(i,cnt+1)
            result.pop()
            visited[i] = 0


n,m = map(int,input().split())

# 순열문제
visited = [0] * (n + 1)
result = []

dfs(0,0)