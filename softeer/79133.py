
def dfs(y,x,cnt,total):
    if cnt == 4:
        print(visited)
        return
    
    dy = [0,1]
    dx = [1,0]

    for d in range(2):
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < n and 0 <= nx < n:
            if visited[ny][nx] == 0:
                for i in range(n):
                    for j in range(n):
                        if visited[i][j] == 0:
                            visited[i][j] = 1
                            dfs(i,j,cnt+1,total+trees[y][x]+trees[ny][nx])
                            visited[i][j]


import sys
input = sys.stdin.readline

n = int(input())
trees = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            dfs(i,j,1,trees[i][j])
            visited[i][j] = 0

'''
4
2 1 3 3
5 1 2 1
2 1 2 3
5 1 1 1 
'''