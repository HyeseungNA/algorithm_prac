n = int(input())
costs = []
for _ in range(n):
    costs.append(int(input()))

total = sum(costs)
costs.sort(reverse=True)
for i in range(n):
    if i  % 3 == 2:
        total -= costs[i]
print(total)
