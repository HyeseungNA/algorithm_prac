import sys
from collections import deque
q = deque()

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    orders = input().split()
    order = orders[0]
    if order == 'push_front':
        q.appendleft(orders[1])
    
    elif order == 'push_back':
        q.append(orders[1])
    
    elif order == 'pop_front':
        if not q:
            print(-1)
        else:
            num = q.popleft()
            print(num)
    
    elif order == 'pop_back':
        if not q:
            print(-1)
        else:
            num = q.pop()
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


