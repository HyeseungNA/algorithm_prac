n = int(input())

a = [0] * 1001

a[1] = 1
a[2] = 3

for i in range(3,1001):
    a[i] = a[i-2] * 2 + a[i-1]

print(a[n] % 10007)