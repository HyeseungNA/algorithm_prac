def solution(m, n, board):
    board = [list(row) for row in board]
    answer = 0
    
    tmp = set()
    while True:
        
        for i in range(m-1):
            for j in range(n-1):
                t = board[i][j]
                
                if t == ' ':
                    continue

                if board[i+1][j] == t and board[i][j+1] == t and board[i+1][j+1] == t:
                    tmp.add((i, j))
                    tmp.add((i+1, j))
                    tmp.add((i, j+1))
                    tmp.add((i+1, j+1))
        
        if tmp:
            answer += len(tmp)
            for i, j in tmp:
                board[i][j] = ' '
            tmp.clear()
            
        else:
            break
        
        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] != ' ' and board[i+1][j] == ' ':
                        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                        moved = 1
            if moved == 0:
                break
    return answer
# 8 5 ["HGNHU", "CRSHV", "UKHVL", "MJHQB", "GSHOT", "MQMJJ", "AGJKK", "QULKK"]