def solution(triangle):
    n = len(triangle)
    
    # dp 리스트 만들기
    dp = [[0] * i for i in range(1,n+1)]
    dp[0][0] = triangle[0][0]
    Max = dp[0][0]
    # dp 초기 상태
    for i in range(1,n):
        dp[i][0] = triangle[i][0] + dp[i-1][0]
        dp[i][-1] =  triangle[i][-1] + dp[i-1][-1]
        Max = max(Max,dp[i][0],dp[i][-1])
    
    # dp 중간
    for i in range(2,n):
        for j in range(len(dp[i])):
            if dp[i][j] == 0:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
                Max = max(Max,dp[i][j])
 
    
    return Max