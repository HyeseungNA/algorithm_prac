import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    orders = input().split()
    order = orders[0]

    if order == 'push':
        value = orders[1]
        stack.append(value)

    elif order == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
