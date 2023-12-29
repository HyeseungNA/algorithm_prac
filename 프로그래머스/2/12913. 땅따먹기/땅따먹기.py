def solution(land):
    answer = 0
    dp = land
    n = len(land)
    for i in range(1,n):
        for j in range(4):
            dp[i][j] += max(dp[i-1][:j] + dp[i-1][j+1:])
    
    
    answer = max(dp[n-1])
    
    return answer