t = int(input())
for _ in range(t):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    if n == 1:
        dp[0][0] = board[0][0]
        dp[1][0] = board[1][0]
    
    elif n == 2:
        dp[0][0] = board[0][0]
        dp[1][0] = board[1][0]
        dp[0][1] = dp[1][0] + board[0][1]
        dp[1][1] = dp[0][0] + board[1][1]
    
    else:
        dp[0][0] = board[0][0]
        dp[1][0] = board[1][0]
        dp[0][1] = dp[1][0] + board[0][1]
        dp[1][1] = dp[0][0] + board[1][1]
        
        for j in range(2,n):
            for i in range(2):
                if i == 0:
                    dp[i][j] = max(dp[0][j-2], dp[1][j-2], dp[1][j-1]) + board[i][j]

                else:
                    dp[i][j] = max(dp[0][j-2], dp[1][j-2], dp[0][j-1]) + board[i][j]



    print(max(dp[0][-1], dp[1][-1]))
   