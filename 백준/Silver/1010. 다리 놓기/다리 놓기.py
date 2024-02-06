t = int(input())
dp = [[0] * 30 for _ in range(30)]

for i in range(30):
    for j in range(30):
        if j == 0 or j == i:
            dp[i][j] = 1
        elif j < i:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

for _ in range(t):
    n,m = map(int,input().split())
    print(dp[m][n])

    
