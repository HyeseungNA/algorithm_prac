word1 = input()
word2 = input()
n = len(word1)
m = len(word2)
dp = [0] * (n)

for i in range(m):
    cnt = 0
    for j in range(n):
        if cnt < dp[j]:
            cnt = dp[j]
        elif word1[j] == word2[i]:
            dp[j] = cnt + 1

print(max(dp))