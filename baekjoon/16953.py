start, end = map(int,input().split())
from collections import deque
lst = []
cnt = 0


def bfs():
    while q:
        print(q)
        start,ne,cnt  = q.popleft()
        if start == end:
            lst.append(cnt)
        elif start > end:
            continue

        start = ne
        n_1 = (ne * 2)
        n_2 = (ne * 10) + 1

        q.append((start,n_1,cnt+1))
        q.append((start,n_2,cnt+1))

q = deque()
n_1 = start * 2
n_2 = (start * 10 ) + 1
cnt = 0
q.append((start,n_1,cnt))
q.append((start,n_2,cnt))

bfs()

if len(lst) == 0:
    print(-1)

else:
    print(min(lst))