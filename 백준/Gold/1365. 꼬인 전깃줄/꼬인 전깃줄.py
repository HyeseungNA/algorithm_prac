def binary_search(target):
    st = 0
    ed = len(LIS) - 1

    while st <= ed:
        mid = (st + ed) // 2

        if LIS[mid] == target:
            return min
        
        elif LIS[mid] < target:
            st = mid + 1
        else:
            ed = mid - 1
    return st

n = int(input())
numbers = list(map(int,input().split()))

# LIS풀이 => 시간초과

LIS = [numbers[0]]
for i in range(1,n):
    if LIS[-1] < numbers[i]:
        LIS.append(numbers[i])
    
    else:
        idx = binary_search(numbers[i])
        LIS[idx] = numbers[i]

print(n - len(LIS))