n = int(input())
height = []
for _ in range(n):
    height.append(int(input()))

LIS = [height[0]]

def binary_search(target):
    st = 0
    ed = len(LIS) - 1

    while st <= ed:
        mid = (st + ed) // 2

        if LIS[mid] < target:
            st = mid + 1
        elif LIS[mid] > target:
            ed = mid - 1
        else:
            return mid

    return st

for i in range(1, n):
    if height[i] > LIS[-1]:
        LIS.append(height[i])
    else:
        idx = binary_search(height[i])
        LIS[idx] = height[i]

print(n - len(LIS))
