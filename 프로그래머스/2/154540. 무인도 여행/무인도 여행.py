from collections import deque
def bfs(y,x,n,m,maps,total,visited):
    q = deque()
    
    q.append([y,x])
    
    while q:
        y,x = q.popleft()
        # print(y,x)
        dy = [-1,0,1,0]
        dx = [0,-1,0,1]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X' and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                total += int(maps[ny][nx])
                # print(total)
                q.append([ny,nx])

    return total
def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[0]* m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                visited[i][j] = 1
                total = int(maps[i][j])
                answer.append(bfs(i,j,n,m,maps,total,visited))
    if not answer:
        answer.append(-1)
    else:
        answer.sort()
    return answer