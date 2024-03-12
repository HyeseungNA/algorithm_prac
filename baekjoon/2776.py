from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    note1 = list(map(int,input().split()))
    d = defaultdict(int)
    for num in note1:
        d[num] += 1
    
    m = int(input())
    note2 = list(map(int,input().split()))

    for num2 in note2:
        if num2 in d:
            print(1)
        else:
            print(0)

