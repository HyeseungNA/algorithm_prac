# import sys
# from collections import defaultdict

# input = sys.stdin.readline
# n,d,k,c = map(int,input().split())
# sushi = []
# for _ in range(n):
#     sushi.append(int(input()))

# sushi.extend(sushi)
# dic = defaultdict(int)
# result = 0

# dic[c] += 1

# left = 0
# right = 0

# while right < k:
#     dic[sushi[right]] += 1
#     right += 1


# while right < len(sushi):
#     result = max(len(dic),result)
#     dic[sushi[left]] -= 1

#     if dic[sushi[left]] == 0:
#         del dic[sushi[left]]
#     dic[sushi[right]] += 1
#     left += 1
#     right += 1

# print(result)



import sys
from collections import defaultdict
input = sys.stdin. readline
N, d, k, c = map(int,input().split())
sushi = []
for _ in range (N):
    sushi.append(int(input()))
sushi += sushi[:k-1]
left = 0
right = 0
Max_cnt = 0
eat = defaultdict(int)
eat[c] += 1
for right in range(len(sushi)):
    eat[sushi[right]]+=1
    if right >= k-1:
        Max_cnt = max(Max_cnt, len(eat))
        eat[sushi[left]]-= 1
        if eat[sushi[left]] == 0:
            del eat[sushi[left]] 
        left += 1

print(Max_cnt)

