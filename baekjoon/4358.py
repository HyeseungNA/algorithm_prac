
from collections import defaultdict
 
trees = defaultdict(int)
total = 0
while True:
    try:
        tree = input()
        trees[tree] += 1
        total += 1
    except:
        break

trees = sorted(trees.items(),key=lambda x:x[0])

for key, value in trees:
    percent = round((value/total * 100),4)
    print(f'{key} {percent:.4f}')