n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

numbers.sort()
result = 0
flag = 1
while flag:
    num = numbers.pop()
    n = len(numbers)
    for i in range(n):
        left = i
        right = n - 1
        total = 0
        while left <= right:
            total = numbers[i] + numbers[left] + numbers[right]

            if total < num:
                left += 1

            elif total > num:
                right -= 1
            
            else:
                result = num
                flag = 0
                break

print(result)