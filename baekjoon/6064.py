import math
n = int(input())
for _ in range(n):
    m,n,x,y = map(int,input().split())
    k = x
    while True:
        if k > math.lcm(m,n):
            print(-1)
            break
        if (k-x) % m == 0 and (k-y) % n == 0:
            print(k)
            break

        k += m

    