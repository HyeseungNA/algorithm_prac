T = int(input())
for _ in range(T):
    n = int(input())
    money = list(map(int,input().split()))
    total = 0
    Max = 0

    for i in range(n-1,-1,-1):
        
        if Max <= money[i]:
            Max = money[i]
        else:
            total += (Max - money[i])
    print(total)

