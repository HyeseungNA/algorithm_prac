n = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
cnt = 0
for i in range(len(numbers)):
    tmp = numbers[:i] + numbers[i+1:]
    left = 0
    right = len(tmp) - 1

    while left < right:
        if tmp[left] + tmp[right] == numbers[i]:
            cnt += 1
            break

        elif tmp[left] + tmp[right] < numbers[i]:
            left += 1
        
        else:
            right -= 1

print(cnt)