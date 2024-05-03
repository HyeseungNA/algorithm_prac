from collections import deque
def bfs(y,x,board,n,m):
    INF = int(12e8)
    visited = [[INF] * m for _ in range(n)]
    q =deque([[y,x,0]])
    visited[y][x] = 0
    while q:

        y,x,cnt = q.popleft() # 현재 위치, 이동 횟수
        
        if board[y][x] == 'G':
            return cnt
        
        dy = [-1,0,1,0]
        dx = [0,-1,0,1]
        
        for i in range(4):
            ny = y
            nx = x
            while True: 
                if 0 <= ny + dy[i] < n and 0 <= nx + dx[i] < m and board[ny + dy[i]][nx + dx[i]] != 'D': 
                    ny += dy[i]
                    nx += dx[i]
                else:
                    break
            
            if cnt + 1 < visited[ny][nx]:
                visited[ny][nx] = cnt + 1
                q.append([ny,nx,cnt+1])
                    
        
                              
                
    return


def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                distance = bfs(i,j,board,n,m)
    if distance:
        answer = distance
    else:
        answer = -1
    return answer

