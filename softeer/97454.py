import sys

# dp로 푸는 문제

n = int(input())
stones = list(map(int,input().split()))
dp = [0] * n

for i in range(n):
    Max = 0
    for j in range(i):
        if stones[i] > stones[j]:
            Max = max(Max, dp[j])

    dp[i] = Max + 1
print(max(dp))
            