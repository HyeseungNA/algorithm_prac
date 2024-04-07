k, n = map(int,input().split())

bags = [[0,0]]

for _ in range(k):
    a,b = map(int,input().split())
    bags.append([a,b])

dp = [[0] * (n+1) for _ in range(k+1)]



for i in range(1,k+1):
    weight, value = bags[i][0],bags[i][1]
    for j in range(1,n+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        
        else:
            dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])
        
    
print(dp[-1][-1])