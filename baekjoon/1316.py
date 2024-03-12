n = int(input())
cnt = 0
for _ in range(n):
    word = list(input())
    com = [word[0]]
    flag = 1
    for i in range(1,len(word)):
        if word[i-1] != word[i]:
            if word[i] not in com:
                com.append(word[i])
            else:
                flag = 0
    if flag == 1:
        cnt += 1
print(cnt)