from collections import deque

def bfs():
    global Min
    q.append(st)
    v[st] = 1

    while q:
        now = q.popleft()
        dy = [now-1, now+1, now * 2]

        if now == ed:
            print(v[now] - 1)
        
        for d in dy:
            if 0 <= d <= Max and v[d] == 0:
                v[d] = v[now] + 1
                q.append(d)

q = deque()
st, ed = map(int,input().split())
Max = 10 ** 5
v = [0] * (Max + 1)

bfs()