n,m = map(int,input().split())
lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
idx1 = 0
idx2 = 0
result = []
while True:
    if idx1 == len(lst1) and idx2 == len(lst2):
        break

    if idx1 == len(lst1) and idx2 < len(lst2):
        result.append(lst2[idx2])
        idx2 += 1
    
    elif idx2 == len(lst2) and idx1 < len(lst1):
        result.append(lst1[idx1])
        idx1 += 1

    else:
        if lst1[idx1] <= lst2[idx2]:
            result.append(lst1[idx1])
            idx1 += 1
        else:
            result.append(lst2[idx2])
            idx2 += 1


print(*result)