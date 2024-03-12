import copy

def count(board):
    global Max
    n = len(board)
    # 열에서 비슷한 사탕 수 찾기
    for i in range(n):
        x = 0
        cnt = 1
        while x < n-1:
            if board[i][x] == board[i][x+1]:
                cnt += 1 
            else:
                cnt = 1
            x += 1
            Max = max(cnt,Max)
    # 행에서 비슷한 사탕 수 찾기
    for j in range(n):
        y = 0
        cnt = 1
        while y < n-1:
            if board[y][j] == board[y+1][j]:
                cnt += 1
            else:
                cnt = 1
            y += 1
            Max = max(cnt,Max)
    return 




def change(y,x):

    dy = [0,1]
    dx = [1,0]

    for m in range(2):
        copy_board = copy.deepcopy(board)
        ny = y + dy[m]
        nx = x + dx[m]

        if 0 <= ny < n and 0 <= nx < n:
            if copy_board[ny][nx] != copy_board[y][x]:
                copy_board[ny][nx], copy_board[y][x] = copy_board[y][x],copy_board[ny][nx]
                count(copy_board)


n = int(input())
board = [list(input()) for _ in range(n)]
Max = 0
for i in range(n):
    for j in range(n):
        change(i,j)
    
print(Max)
'''
6
CCYYCC
YYCCYY
CCYYCC
YYCCYY
CCYYCC
YYCCYY
'''