import copy
n = int(input())
first = list(input())

result = 0 # 비슷한 단어 개수

for _ in range(n-1):
    com = first[:]
    word = list(input())
    cnt = 0
    for w in word:
        if w in com:
            com.remove(w)
        else:
            cnt += 1
    
    if cnt < 2 and len(com) < 2:
        result += 1




print(result)