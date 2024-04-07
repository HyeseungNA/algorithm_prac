n,k = map(int,input().split())
cnt = 0

waters = bin(n)[2:].count('1')
while n <= 10 ** 7 and waters > k:
    n += 1
    cnt += 1
    waters = bin(n)[2:].count('1')

if cnt == 0:
    print(-1)
else:
    print(cnt)