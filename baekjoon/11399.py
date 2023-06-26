n = int(input())
time = list(map(int,input().split()))

total_list = []

time.sort()
total = 0

for i in range(len(time)):
    total += time[i]
    total_list.append(total)

print(sum(total_list))