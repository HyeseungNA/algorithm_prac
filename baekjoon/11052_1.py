n = int(input())
cards = [0]
cards += list(map(int,input().split()))
dp = [0] * (n+1)

for i in range(1,n+1):
    for j in range(i+1):
        dp[i] = max(dp[i], dp[j] + cards[i-j])

print(dp[-1])
