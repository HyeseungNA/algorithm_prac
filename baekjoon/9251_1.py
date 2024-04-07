a = input()
b = input()
h = len(a)
w = len(b)


board = [[0] * (w+1) for _ in range(h + 1)]

for i in range(1,h+1):
    for j in range(1,w+1):
        if a[i-1] == b[j-1]:
            board[i][j] = board[i-1][j-1] + 1
        else:
            board[i][j] = max(board[i-1][j], board[i][j-1])

print(board[h][w])