n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))


dp = [0] * n
dp[0] = wine[0]
if n > 1:
    dp[1] = wine[0] + wine[1]
    if n > 2:
        dp[2] = max(dp[0] + wine[2], wine[1]+wine[2],dp[1])

        # 전전전 최대 + 전 와인 + 현재와인
        # 전전 최대 + 현재 와인
        # 전 최대
        for i in range(3,n):
            dp[i] = max(dp[i-3] + wine[i-1]+wine[i], dp[i-2]+wine[i],dp[i-1])

print(max(dp))