n = int(input())

for i in range(1,n):
    lst  = list(map(int,str(i)))
    if n == i + sum(lst):
        print(i)
        exit()

print(0)

