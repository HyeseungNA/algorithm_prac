def dfs(point):
    result = [point]
    while lst[point] != 0:
        result.append(lst[point])
        point = lst[point]
    
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    lst = [0]  * (n+1)
    for _ in range(n-1):
        c,p = map(int,input().split())
        lst[p] = c
    a,b = map(int,input().split())
    a_parents = dfs(a)
    b_parents = dfs(b)
    
    for num in a_parents:
        if num in b_parents:
            print(num)
            break
    
    