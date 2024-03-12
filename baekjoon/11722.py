def binary_search(target):
    st = 0 
    ed = len(LIS) - 1

    while st <= ed:
        mid = (st + ed) // 2

        if LIS[mid] == target:
            return mid
        elif LIS[mid] < target:
            st = mid + 1
        else:
            ed = mid - 1
    
    return st


n = int(input())
numbers = list(map(int,input().split()))
reversed_numbers = numbers[::-1]
LIS = [reversed_numbers[0]]


for i in range(1,n):
    if reversed_numbers[i] > LIS[-1]:
        LIS.append(reversed_numbers[i])
    else:
        idx = binary_search(reversed_numbers[i])
        LIS[idx] = reversed_numbers[i]

print(len(LIS))