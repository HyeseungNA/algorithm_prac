from collections import deque

def move(y, x, idx):
    global cnt, snake
    move = [[-1,0],[0,1],[1,0],[0,-1]]  
    dy = 0
    dx = 1
    time, order = orders.popleft()
    while True:
        y += dy
        x += dx
        cnt += 1
        if y < 0 or y >= n or x < 0 or x >= n:
            break
        if board[y][x] == 2:  # 자기 몸이랑 부딪히거나, 벽에 닿으면 멈추기
            break
        else:
            if board[y][x] == 0:  # 새로운 곳에 사과가 엇다면
                tail_y, tail_x = snake.popleft()  # 꼬리 줄여주기
                board[tail_y][tail_x] = 0

            if cnt == int(time):
                if order == 'D':  # 방향 정해주기
                    idx = (idx + 1) % 4
                else:
                    idx = (idx - 1) % 4
                dy = move[idx][0]
                dx = move[idx][1]
                if orders:  # 명령이 남아 있다면
                    time, order = orders.popleft()
            snake.append([y,x])
            board[y][x] = 2

    return cnt


n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
board[0][0] = 2  # 자기 자신
snake = deque([[0,0]])
for _ in range(k):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 1

l = int(input())
orders = deque()
cnt = 0

for _ in range(l):
    t, o = input().split()
    orders.append([t, o])

print(move(0, 0, 1))  # 뱀 y, 뱀x, 바라보는 방향
