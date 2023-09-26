def dfs(now,cnt):

    if cnt == m:
        print(*result)
    
    for i in range(now,n+1):
        result.append(i)
        dfs(i+1,cnt+1)
        result.pop()



# 조합문제
n,m = map(int,input().split())

result = []

dfs(1,0)