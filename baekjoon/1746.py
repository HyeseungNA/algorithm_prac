n,m = map(int,input().split())


see = []
result= []
dic = {}
for _ in range(n):
    listen = input()
    if listen not in dic:
        dic[listen] = 1

for _ in range(m):
    word = input()
    if word in dic:
        result.append(word)



result.sort()
print(len(result))
for re in result:
    print(re)