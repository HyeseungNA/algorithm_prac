from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
A = []
B = []
C = []
D = []

for _ in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)


AB = [i + j for i in A for j in B]
CD = [i + j for i in C for j in D]

CD = Counter(CD)

cnt = 0
for num in AB:
    if CD[-num]:
        cnt += CD[-num]
    

print(cnt)