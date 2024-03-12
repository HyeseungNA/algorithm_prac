from collections import defaultdict
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
numbers = list(map(int,input().split()))


left = 0
right = left
Max_length = 0
dic = defaultdict(int)
while left < n and right < n:
    if dic[numbers[right]] < k:
        dic[numbers[right]] += 1
        right += 1
    else:
        Max_length = max(Max_length,right - left)
        dic[numbers[left]] -= 1
        left += 1
    
# 마지막 예외 확인
if dic[right-1] <= k:
    Max_length = max(Max_length,right - left)
print(Max_length)
'''
29 3
1 2 3 4 5 6 7 8 9 1 1 11 1 14 15 16 23 43 24 53 24 25 99 29 36 45 64 69 45
'''