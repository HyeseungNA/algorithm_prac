
n,m = map(int,input().split())

dic = {}
cnt = 0
for _ in range(n):
    word = input()
    dic[word] = 1

for _ in range(m):
    com = input()
    if com in dic:
        cnt += 1

print(cnt)