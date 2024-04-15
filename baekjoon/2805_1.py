def binary_search():
    st = 0
    ed = max(trees)

    while st <= ed:
        mid = (st + ed) // 2
        
        total = 0
        for tree in trees:
            if tree > mid:
                total += (tree - mid)
        
        if total >= m:
            st = mid + 1
        else:
            ed = mid - 1
    
    return ed




n,m = map(int,input().split())
trees = list(map(int,input().split()))
trees.sort()

print(binary_search())
