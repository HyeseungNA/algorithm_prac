def check(st,ed):

    while st <= ed:
        if word[st] == word[ed]:
            st += 1
            ed -= 1
        else:
            return False
    return True


n = int(input())
for _ in range(n):
    word = list(input())
    reversed_word = word[::-1]

    if word == reversed_word:
        print(0)
        continue

    else:
        st = 0 
        ed = len(word) - 1

        while st <= ed:
            if word[st] == word[ed]:
                st += 1
                ed -= 1
            else:
                result1 = check(st+1,ed)
                result2 = check(st,ed-1)
                if result1 or result2:
                    print(1)
                    break
                else:
                    print(2)
                    break
                
'''
1
xyyyyxy
'''