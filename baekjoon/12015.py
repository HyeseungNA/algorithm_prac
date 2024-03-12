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
LIS= [numbers[0]]


for i in range(1,n):
    if numbers[i] > LIS[-1]:
        LIS.append(numbers[i])
    else:
        idx = binary_search(numbers[i])
        LIS[idx] = numbers[i]
print(len(LIS))
