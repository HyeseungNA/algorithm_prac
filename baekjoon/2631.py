
n = int(input())
height = []
for _ in range(n):
    height.append(int(input()))


LIS = [height[0]]
# dp = [1] * (n+1)

# for i in range(1,n):
#     for j in range(i):
#         if height[j] < height[i]:
#             dp[i] = max(dp[i], dp[j]+ 1)

# print(n - max(dp))

def binary_search(target):
    st = 0
    ed = len(LIS) - 1

    while st <= ed:
        mid = (st + ed) // 2

        if LIS[mid] == target:
            return mid
        
        elif LIS[mid] < target:
            st = mid + 1

        else:
            ed = mid - 1

    return st

for i in range(1,n):
    if LIS[-1] < height[i]:
        LIS.append(height[i])
    else:
        idx = binary_search(height[i])
        LIS[idx] = height[i]
print(LIS)
print(n - len(LIS))