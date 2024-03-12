n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
dic1 = {}
dic2 = {}

for num in a:
    if num not in dic1:
        dic1[num] = 1
    else:
        dic1[num] += 1

for num2 in b:
    if num2 not in dic2:
        dic2[num2] = 1
    else:
        dic2[num2] += 1
cnt = 0
cnt2 = 0
for el in dic1:
    if el not in dic2:
        cnt += 1
for el2 in dic2:
    if el2 not in dic1:
        cnt2 += 1

print(cnt+cnt2)