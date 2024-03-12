N, M = map(int, input().split())

A, B = [], []

for _ in range(N):
    types, coin = input().split()
    if types == 'A':
        A.append(coin)
    else:
        B.append(coin)


B_col = [(0,0)]
for i in B:
    tmp = [(coin + i, count + 1) for coin, count in B_col if (coin + i) <= M]
    print(tmp)
    B_col += tmp
DP_B = [99999 for _ in range(M + 1)]

for coin, count in B_col:
    if DP_B[coin] > count:
        DP_B[coin] = count

DP_A = [99999 for _ in range(M + 1)]
DP_A[0] = 0
q = [(0,0)]
index = 0
while q:
    coin, count = q.pop()
    count += 1
    for A_coin in A:
        if A_coin + coin < M+1 and DP+A[A_coin + coin] < count:
            DP_A[A_coin + coin] = count
        q.append((A_coin + coin, count))

res = []
if DP_A[-1] != 99999:
    res.append(DP_A[-1])
if DP_B[-1] != 99999:
    res.append(DP_B[-1])

for i in range(1, M):
    if DP_A[i] != 99999 and DP_B[M-i] != 99999:
        res.append(DP_A[i] + DP_B[M-i])

if res:
    print(min(res))
else:
    print(-1)
