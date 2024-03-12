def dfs(now,cnt,total):
    global Max

    if cnt == n:
        Max = max(Max,total)
        return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i,cnt+1,total + abs(numbers[now]-numbers[i]))
            visited[i] = 0


n = int(input())
numbers = list(map(int,input().split()))
n = len(numbers)
Max = 0
visited = [0] * n

for i in range(n):
    visited[i] = 1
    dfs(i,1,0)
    visited[i] = 0
print(Max)