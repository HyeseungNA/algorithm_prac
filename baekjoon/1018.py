def count_changes(start_color, y, x):
    changes = 0
    for i in range(y,y+8):
        for j in range(x,x+8):
            if (i + j) % 2 == 0:
                if board[i][j] != start_color:
                    changes += 1
            else:
                if board[i][j] == start_color:
                    changes += 1
    return changes

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
Min = int(12e9)

for i in range(n - 7):
    for j in range(m - 7):
        result_black = count_changes('B', i, j)
        result_white = count_changes('W', i, j)
        Min = min(result_black, result_white, Min)

print(Min)
