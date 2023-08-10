def solution(n):
    if n < 3:
        return n
    
    else:
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3,n+1):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n] % 1234567

solution(1)