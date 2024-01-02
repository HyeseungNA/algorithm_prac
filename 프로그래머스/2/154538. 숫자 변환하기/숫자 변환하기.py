from collections import deque
def bfs(x,y,n):
    q = deque()
    q.append(x)
    visited = [0] * (y + 1)
    
    while q:
        now = q.popleft()
        
        if now == y:
            return visited[now]
        move = [now * 2, now * 3, now + n]
        for m in move:
            if m <= y and visited[m] == 0:
                q.append(m)
                visited[m] = visited[now] + 1

    return -1


def solution(x, y, n):
    
    return bfs(x,y,n)
    
    
