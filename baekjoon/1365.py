from bisect import bisect_left

n = int(input())
numbers = list(map(int,input().split()))

# LIS풀이 => 시간초과

LIS = [numbers[0]]
for i in range(1,n):
    if LIS[-1] < numbers[i]:
        LIS.append(numbers[i])
    
    else:
        idx = bisect_left(LIS,numbers[i])
        LIS[idx] = numbers[i]

