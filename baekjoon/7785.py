from collections import defaultdict
n = int(input())
dic = defaultdict(int)
for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        dic[name] = 1
    
    else:
        del dic[name]
    
sorted_dic = sorted(dic,reverse=True)
for n in sorted_dic:
    print(n)