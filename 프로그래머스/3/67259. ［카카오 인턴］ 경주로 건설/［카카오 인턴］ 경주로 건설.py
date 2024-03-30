from collections import deque
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(board,di,n):
    costs = [[int(12e9)] * n for _ in range(n)]
    costs[0][0] = 0
    q = deque()
    q.append([0,0,0,di]) # y좌표, x좌표, 비용, 방향
    
    while q:
        y,x,c,di = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                if di == i:
                    nc = c + 100
                else:
                    nc = c + 600
                
                if nc <= costs[ny][nx]:
                    costs[ny][nx] = nc
                    
                    q.append([ny,nx,nc,i])

    return costs[-1][-1]
                    
                    
        
        
        
    return




def solution(board):
    answer = 0
    n = len(board)
    answer = min(bfs(board,0,n), bfs(board,1,n))
    return answer