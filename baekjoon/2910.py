n,c = map(int,input().split())
numbers = list(map(int,input().split()))

dic = dict()

for num in numbers:
    if num not in dic:
        dic[num] = 0
    dic[num] += 1

dic = sorted(dic.items(), key = lambda x:x[1], reverse= True)


for a,b in dic:
    for _ in range(b):
        print(a,end=' ')