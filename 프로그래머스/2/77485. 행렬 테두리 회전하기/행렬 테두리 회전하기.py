def solution(rows, columns, queries):
    board = [ [(row * columns) + (col + 1) for col in range(columns)] for row in range(rows)]
    answer = []
    for query in queries:
        y1,x1,y2,x2 = query[0]-1,query[1]-1,query[2]-1,query[3]-1
        tmp = board[y1][x2]
        Min = tmp
        # 오른쪽으로 밀기
        for i in range(x2,x1,-1):
            Min = min(Min,board[y1][i-1])
            board[y1][i] = board[y1][i-1]
        
        # 위로 밀기
        for i in range(y1,y2):
            Min = min(Min,board[i+1][x1])
            board[i][x1] = board[i+1][x1]
        

        
        # 왼쪽으로 밀기
        for i in range(x1,x2):
            Min = min(Min,board[y2][i+1] )
            board[y2][i] = board[y2][i+1]
    
 
        # 아래로 밀기
        for i in range(y2,y1,-1):
            Min = min(Min,board[i-1][x2] )
            board[i][x2] = board[i-1][x2]
        
        board[y1+1][x2] = tmp
        
        answer.append(Min)
      
        
    return answer