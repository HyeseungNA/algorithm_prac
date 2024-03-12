n = int(input())
waters = list(map(int,input().split()))
left = 0
right = len(waters) - 1
result = []
Min = 2000000000
while left < right:
    total = waters[left] + waters[right]
    if abs(total) < abs(Min):
        result = [waters[left], waters[right]]
        Min = total

    if total < 0:
        left += 1
    
    else:
        right -= 1

print(*result)