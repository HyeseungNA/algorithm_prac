def dfs(now, result, cnt):
    if cnt == 6:
        print(*result)
        return
    
    for i in range(now+1,n):
        dfs(i,result+[numbers[i]],cnt+1)


while True:
    arr = list(map(int,input().split()))
    n = arr[0]
    numbers = arr[1:]
    for i in range(n):
        dfs(i,[numbers[i]],1)
    
    if n == 0:
        break
    print()