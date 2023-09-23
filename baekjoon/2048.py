# 다음이 빈공간이면 이동
# 다음이 같은 숫자이면 합체
# 합체했으면 체크하기
# 상하좌우 한번씩 긔

def move(y,x,dy,dx):

    while 0 <= y + dy < n and 0 <= x + dx < n:

        # 다음 값이랑 같으면 합체하고 체크해주기
        if boards[y+dy][x+dx] == boards[y][x]:
            if check[y+dy][x+dx] == 0:
                boards[y+dy][x+dx] = 2 * boards[y+dy][x+dx]
                boards[y][x] = 0
                check[y+dy][x+dx] = 1
        
        # 다음 값이 빈 공간이면 이동해주기
        if boards[y+dy][x+dx] == 0:
            boards[y+dy][x+dx] = boards[y][x]
            boards[y][x] = 0

        y += dy
        x += dx

    return boards

n = int(input())
boards = [list(map(int,input().split())) for _ in range(n)]
check = [[0] * n for _ in range(n)]

# 사방탐색
dy = [-1,0,1,0]
dx = [0,-1,0,1]

for i in range(4):
    for y in range(n):
        for x in range(n):
            result = move(y,x,dy[i],dx[i])

Max = 0
for i in range(n):
    Max < max(boards[i])
    Max = max(boards[i])

print(Max)