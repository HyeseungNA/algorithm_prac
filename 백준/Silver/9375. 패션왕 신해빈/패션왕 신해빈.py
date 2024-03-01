from collections import defaultdict
t = int(input())


for _ in range(t):
    n = int(input())
    dic = defaultdict(int)
    result = 1
    for _ in range(n):
        name, type = input().split()
        dic[type] += 1


    for value in dic.values():
        result *= (value + 1)
    
    print(result - 1)