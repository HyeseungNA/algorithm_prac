from collections import defaultdict
n,m = map(int,input().split())
dic = defaultdict(int)
for _ in range(n):
    site, password = input().split()
    dic[site] = password

for _ in range(m):
    find = input()
    print(dic[find])