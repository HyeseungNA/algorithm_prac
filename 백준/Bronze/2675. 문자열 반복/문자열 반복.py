t = int(input())
for _ in range(t):
    n,word = input().split()
    result = ''
    for w in word:
        result += int(n) * w
    
    print(result)