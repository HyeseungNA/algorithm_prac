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
    

if dic[right-1] <= k:
    Max_length = max(Max_length,right - left)
print(Max_length)