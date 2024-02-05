t = int(input())
dp = [0] * 100
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
idx = 5
st = 0
while idx < 100:
    dp[idx] = dp[st] + dp[idx-1]
    st += 1
    idx += 1

for _ in range(t):
    n = int(input())
    print(dp[n-1])

