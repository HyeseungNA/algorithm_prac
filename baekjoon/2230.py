n,m = map(int,input().split())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

numbers.sort()

left = 0
right = 0
Max = 2000000000


while left <= right and left < n and right < n:
    total = numbers[right] - numbers[left]

    if total < m:
        right += 1
    
    elif total == m:
        Max = m
        break
    else:
        left += 1
        Max = min(Max,total)

print(Max)
'''
7 4
1
8
15
16
17
18
22
'''