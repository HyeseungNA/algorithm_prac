def binary_search(target):
    st = 1
    ed = max(lans)

    while st <= ed:
        mid = (st + ed) // 2
        
        result = 0
        for lan in lans:
            result += (lan // mid)
        
        if result < target:
            ed = mid - 1
        
        else:
            st = mid + 1
    
    return ed


n,k = map(int,input().split())
lans = []
for _ in range(n):
    lans.append(int(input()))

print(binary_search(k))