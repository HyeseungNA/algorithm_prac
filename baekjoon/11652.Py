from collections import defaultdict
n = int(input())
dic = defaultdict(int)
for _ in range(n):
    dic[int(input())] += 1


sorted_dic = sorted(dic.items(), key=lambda x:(-x[1],x[0]))
print(sorted_dic[0][0])