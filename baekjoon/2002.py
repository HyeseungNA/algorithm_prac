from collections import defaultdict, deque

n = int(input())

enter = deque()
out = deque()
for i in range(n):
    enter.append(input())

for j in range(n):
    out.append(input())


cnt = 0
while out:
    now = out.popleft()
    if now == enter[0]:
        enter.popleft()
    else:
        cnt += 1
        enter.remove(now)


print(cnt)
