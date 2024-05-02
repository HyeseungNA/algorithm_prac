from collections import deque

def bfs(y,x,places):
    q = deque()
    q.append([y,x,0])
    visited = [[0] * 5 for _ in range(5)]
    visited[y][x] = 1
    
    
    while q:
        y,x,cnt = q.popleft()
        
        if places[y][x] == 'P'and 1 <= cnt <= 2:
            return False
            
        dy = [-1,0,1,0]
        dx = [0,-1,0,1]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5 and places[ny][nx] != 'X' and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append([ny,nx,cnt+1])
                
    return True

def solution(places):
    answer = []
    
    for place in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs(i,j,place):
                        flag = 0
                    if flag == 0:
                        break
            if flag == 0:
                break
        answer.append(flag)
                    
        
                    
    return answer