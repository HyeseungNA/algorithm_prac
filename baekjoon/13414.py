
k,l = map(int,input().split())
d = {}

for i in range(l):
    number = input()
    d[number] = i


sorted_d = sorted(d.items(),key=lambda x:x[1])

if k > len(sorted_d):
    k = len(sorted_d)

for i in range(k):
    print(sorted_d[i][0])



