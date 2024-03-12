from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    orders = input().split()
    order = orders[0]

    if order == 'push':
        q.append(orders[1])
    
    elif order == 'pop':
        if not q:
            print(-1)
        else:
            num = q.popleft()
            print(num)
    elif order == 'size':
        print(len(q))
    
    elif order == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    
    elif order == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    
    else:
        if not q:
            print(-1)
        else:
            print(q[-1])


