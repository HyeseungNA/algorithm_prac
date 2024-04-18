n,s = map(int,input().split())
numbers = list(map(int,input().split()))

left = 0
right = 0
total = numbers[left]
Min = int(12e8)
while left <= right and right < n:
    if total < s:
        right += 1
        if right <= n - 1:
            total += numbers[right]
    
    else:
        Min = min(Min,right - left + 1)
        total -= numbers[left]
        left += 1


if Min == int(12e8):
    print(0)

else:

    print(Min)