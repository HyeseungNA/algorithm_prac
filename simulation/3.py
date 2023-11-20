n,m = map(int,input().split())
d = [[0] * m for _ in range(n)]

y,x,direction = map(int,input().split())
d[y][x] = 1

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

cnt = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dx[direction]

    if d[ny][nx] == 0 and array[ny][nx] == 0:
        d[ny][nx] = 1
        y = ny
        x = nx
        cnt += 1
        turn_time = 0
    else:
        turn_time += 1
    
    if turn_left == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[ny][nx] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
    
print(cnt)