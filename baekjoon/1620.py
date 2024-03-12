import sys
input = sys.stdin.readline
n,m = map(int,input().split())

pocketmons = {}
for i in range(n):
    name = input().strip()
    pocketmons[name] = i+1
    pocketmons[i+1] = name




for _ in range(m):
    word = input().rstrip()
    if word.isdigit():
        idx = int(word)
        print(pocketmons[idx])
    else:
        print(pocketmons[word])
    
        