n = int(input())
dp = [[0] * i for i in range(1,n+1)]
Max = int(-12e8)
graph = [list(map(int,input().split())) for _ in range(n)]

if n == 1:
    dp[0][0] = graph[0][0]
elif n == 2:
    dp[0][0] = graph[0][0]
    dp[1][0] = dp[0][0] + graph[1][0]
    dp[1][1] = dp[0][0] +  graph[1][1]
else:
    dp[0][0] = graph[0][0]
    dp[1][0] = dp[0][0] + graph[1][0]
    dp[1][1] = dp[0][0] +  graph[1][1]
    for i in range(2,n):
        for j in range(len(graph[i])):
            if j == 0:
                dp[i][0] = dp[i-1][0] + graph[i][0]
            elif 1 <= j < len(graph[i]) - 1:
                dp[i][j] = max(dp[i-1][j-1] + graph[i][j], dp[i-1][j] + graph[i][j])
            else:
                dp[i][j] = dp[i-1][j-1] + graph[i][j]

for i in range(n):
    Max = max(Max,dp[n-1][i])

print(Max)

'''
11
1
1 0
0 1 1
1 1 0 0
0 1 1 0 1
0 1 0 0 0 1
1 0 1 1 1 1 1
1 1 1 0 0 1 1 0
0 1 1 1 0 1 1 0 0
1 1 0 1 1 0 0 1 1 0
1 0 0 1 1 1 0 1 1 1 1
'''