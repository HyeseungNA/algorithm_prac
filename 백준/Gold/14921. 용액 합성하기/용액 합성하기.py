n = int(input())
waters = list(map(int,input().split()))
left = 0
right = n - 1
result = int(1e9)
while left < right:
    total = waters[left] + waters[right]
    if abs(total) < abs(result):
        result = total
    if total < 0:
        left += 1
    elif total == 0:
        result = 0
        break
    else:
        right -= 1

print(result)