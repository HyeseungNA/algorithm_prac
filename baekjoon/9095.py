def dfs(now):
    global cnt
    total.append(now)
    if sum(total) == n:
        # print(total)
        cnt += 1
        return
    elif sum(total) > n: # 총합이 sum보다 크면 그냥 return
        return

    for i in range(1,4):
        dfs(i)
        total.pop()

    

T = int(input())
for _ in range(T):
    n = int(input())
    lst = [0,1,2,3]
    total = []
    cnt = 0 # 가능한 개수
    for i in range(1,4):
        dfs(i)
        total.pop()
    print(cnt)