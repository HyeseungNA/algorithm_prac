from collections import deque
def bfs(st,ed,n,m,maps):
    
    visited = [[0] * m for _ in range(n)]
    st_y,st_x = st[0],st[1]
    ed_y,ed_x = ed[0],ed[1]
    
    visited[st_y][st_x] = 1
    q = deque([[st_y,st_x,0]])
   
    while q:
        y,x,cnt = q.popleft()
        if y == ed_y and x == ed_x:
            return cnt
        
        dy = [-1,0,1,0]
        dx = [0,-1,0,1]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X' and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append([ny,nx,cnt+1])



def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = 0
    st = []
    le = []
    ed = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                st = [i,j]
            elif maps[i][j] == 'L':
                le = [i,j]
            elif maps[i][j] == 'E':
                ed = [i,j]

    distance1 = bfs(st,le,n,m,maps)
    
    distance2 = bfs(le,ed,n,m,maps)
    if distance1 and distance2:
        answer = distance1 + distance2
    else:
        answer = -1
    return answer