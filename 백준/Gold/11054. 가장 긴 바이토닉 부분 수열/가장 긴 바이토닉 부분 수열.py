n = int(input())
increased = list(map(int,input().split()))
decreased = increased[::-1]
in_dp = [1] * n
de_dp = [1] * n
result = 0

for i in range(n):
    for j in range(i):
        if increased[i] > increased[j]:
            in_dp[i] = max(in_dp[i], in_dp[j] + 1)
        
        if decreased[i]> decreased[j]:
            de_dp[i] = max(de_dp[i], de_dp[j]+1)
de_dp = de_dp[::-1]

for i in range(n):
    result = max(result,in_dp[i]+ de_dp[i])

print(result - 1)