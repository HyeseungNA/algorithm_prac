from collections import deque
q = deque()
n,k = map(int,input().split())
q = deque([i for i in range(1,n+1)])
cnt = 0
result = []
while q:
    num = q.popleft()
    cnt += 1
    if cnt == k:
        result.append(num)
        cnt = 0
    else:
        q.append(num)

print(str(result).replace('[','<').replace(']','>'))