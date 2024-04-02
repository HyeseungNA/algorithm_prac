n,k = map(int,input().split())
cnt = 0

waters = bin(n)[2:].count('1')
while waters > k:
    n += 1
    cnt += 1
    waters = bin(n)[2:].count('1')

print(cnt)