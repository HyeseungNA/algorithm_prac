def palidrome(word,l,r) :
    global cnt
    cnt += 1
    if l >= r:
        return 1
    if word[l] != word[r]:
        return 0
    else:
        return palidrome(word, l+1, r-1)

n = int(input())
for _ in range(n):
    word = input()
    cnt = 0
    print(palidrome(word,0, len(word)-1), cnt)



