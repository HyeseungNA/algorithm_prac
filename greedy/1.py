# n, m, k = list(map(int,input().split()))
# lst = list(map(int,input().split()))
# result = 0

# lst.sort()

# first = lst[n-1]
# second = lst[n-2]

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1

#     if m == 0:
#         break
#     result += second
#     m -= 1

# print(result)

n, m, k = list(map(int,input().split()))
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

count = (m // (k+1) * k ) + m % (k+1)

result += count * first
result += (m- count) * second

print(result)