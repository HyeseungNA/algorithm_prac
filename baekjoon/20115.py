n = int(input())

juice = list(map(int,input().split()))
juice.sort(reverse=True)

idx = 0
total = juice[idx]

while idx < n-1:
    j = max(total , juice[idx+1]) + min(total, juice[idx+1]) / 2
    idx += 1
    total = j
print(total)

