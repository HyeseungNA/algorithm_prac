from collections import deque
def bfs(now):
    global result
    q = deque()
    q.append([now,0])
    visited[now] = 1

    while q:
        now,cnt =q.popleft()
        if now == g:
            result = cnt
            break

        dy = [u,-d]
        for i in range(2):
            ny = now + dy[i]
            if 0 < ny <= f and visited[ny] == 0:
                visited[ny] = 1
                q.append([ny,cnt+1])

    return


f,s,g,u,d = map(int,input().split())
visited = [0] * (f+1)
result = -1
bfs(s)

if result == -1:
    print('use the stairs')
else:
    print(result)
