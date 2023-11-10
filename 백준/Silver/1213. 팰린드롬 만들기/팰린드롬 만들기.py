word = input()
palin = []
temp = [] # 펠린드롬 감별

for w in word:
    if w not in temp:
        palin.append(w)
        temp.append(w)
    else:
        temp.remove(w)

if len(temp) > 1:
    print("I'm Sorry Hansoo")
else:
    palin.sort()
    if temp:      
        palin.remove(*temp)
    result = palin + temp + palin[::-1]
    print(''.join(result))