n = int(input())
numbers = list(map(int,input().split()))
x = int(input())

numbers.sort()
cnt = 0
left = 0
right = len(numbers) - 1

while left < right:
    total = numbers[right] + numbers[left]

    if total >= x:
        if total == x:
            cnt += 1
        right -= 1
    else:
        left += 1

print(cnt)