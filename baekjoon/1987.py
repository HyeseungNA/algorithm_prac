import sys
input = sys.stdin.readline
def dfs(y,x,cnt):
    global Max,visited
    Max = max(cnt, Max)
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]


    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and visited[ord(board[ny][nx])- 65] == 0:
            visited[ord(board[ny][nx])- 65] = 1
            dfs(ny,nx,cnt+1)
            visited[ord(board[ny][nx])- 65] = 0
    return

n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
visited = [0] * 26
Max = 0
visited[ord(board[0][0]) - 65] = 1
dfs(0,0,1) # 현재 좌표, 방문, cnt
print(Max)