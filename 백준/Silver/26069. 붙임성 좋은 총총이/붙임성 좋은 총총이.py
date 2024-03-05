from collections import defaultdict
d = defaultdict(int)
d["ChongChong"] = 1
n = int(input())
for _ in range(n):
    name1, name2 = input().split()

    if name1 in d:
        d[name2] += 1
    
    elif name2 in d:
        d[name1] += 1

print(len(d))