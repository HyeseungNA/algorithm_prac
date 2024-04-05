n = int(input())
dp = [0] * (n+1)
wines = [0]

for _ in range(n):
    wines.append(int(input()))

if n == 1:
    dp[1] = wines[1]
    print(dp[1])

elif n == 2:
    dp[1] = wines[1]
    dp[2] = dp[1] + wines[2]
    print(wines[1] + wines[2])

elif n == 3:
    dp[1] = wines[1]
    dp[2] = dp[1] + wines[2]
    dp[3] = max(dp[1] + wines[3] , dp[2], wines[2] + wines[3])
    print(dp[3])

else:
    dp[1] = wines[1]
    dp[2] = dp[1] + wines[2]
    dp[3] = max(dp[1] + wines[3] , dp[2], wines[2] + wines[3])

    for i in range(4,n+1):
        dp[i] = max(dp[i], dp[i-2] + wines[i], dp[i-1], dp[i-3] + wines[i-1] + wines[i])

    print(max(dp))
