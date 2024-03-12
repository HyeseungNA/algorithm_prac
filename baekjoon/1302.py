from collections import defaultdict
n = int(input())
dic = defaultdict(int)
for _ in range(n):
    book = input()
    dic[book] += 1


sorted_book = sorted(dic.items(), key=lambda x:(-x[1],x[0]))

print(sorted_book[0][0])