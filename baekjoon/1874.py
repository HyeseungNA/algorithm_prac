from collections import deque
n = int(input())
compare = [] # 비교할 리스트
stack = []
compute = []
result = []
for _ in range(n):
    compare.append(int(input()))
numbers = deque([i for i in range(1,n+1)])
i = 0

while i < len(compare):
    if not stack:
        if numbers:
            num = numbers.popleft()
            stack.append(num)
            compute.append('+')
        else:
            break
    if stack:
        if stack[-1] == compare[i]: # 같으면
            result.append(stack[-1])
            stack.pop()
            compute.append('-')
            i += 1
        else:
            if numbers:
                num = numbers.popleft()
                if num <= compare[i]:
                    stack.append(num)
                    compute.append('+')
                else:
                    stack.pop()
                    compute.append('-')
            else:
                break
if compare == result:
    for com in compute:
        print(com)
else:
    print('NO')

'''
8
2
4
7
5
3
1
8
6
NO

'''