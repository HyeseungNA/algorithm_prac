n = int(input())

triangles = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * (i+1) for i in range(n)]

if n == 1:
    dp[0][0] = triangles[0][0]
if n >= 2:
    dp[0][0] = triangles[0][0]
    dp[1][0] = triangles[0][0] + triangles[1][0]
    dp[1][1] = triangles[0][0] +  triangles[1][1]
    for i in range(2,n):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangles[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangles[i][j]

            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangles[i][j]

print(max(dp[-1]))

'''
4
1
0 1
0 0 1
100 0 0 0
'''