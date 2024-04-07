t = int(input())
dp = [[1] * (i+1) for i in range(31)]

for i in range(31):
    for j in range(1,i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]


for _ in range(t):
    n,m = map(int,input().split())
    print(dp[m][n])
