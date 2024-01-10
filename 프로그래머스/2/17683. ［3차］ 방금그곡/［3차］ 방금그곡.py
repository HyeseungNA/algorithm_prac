def solution(m, musicinfos):
    answer = []
    com1 = []
    result = ''
    j = 0
    while j < len(m):
            word = ''
            if j <= len(m) - 2 and (m[j] != '#' and m[j+1] == '#'):
                word = m[j] + m[j+1]
                j += 1
            else:
                word = m[j]
            
            com1.append(word)
            j += 1
    # print(com1)
    for music in musicinfos:
        flag = 0
        music = music.split(',')
        melody = []
        st = music[0]
        ed = music[1]
        name = music[2]
        sen = music[3]
        time = int(ed[:2]) * 60 + int(ed[3:]) - (int(st[:2]) * 60 + int(st[3:]))
        
        i = 0
        while i < len(sen):
            word = ''
            if i <= len(sen) - 2 and (sen[i] != '#' and sen[i+1] == '#'):
                word = sen[i] + sen[i+1]
                i += 1
            else:
                word = sen[i]
            
            melody.append(word)
            i += 1
        n,na = divmod(time,len(melody))
        melody = melody * n + melody[:na]
        # print(melody,'___')
        
        for i in range(len(melody) - len(com1) + 1):
            com2 = melody[i:i+len(com1)]
            
            if com1 == com2:
                flag = 1
                break
        if flag == 1:
            answer.append([time,name])
        
            
    answer = sorted(answer,key=lambda x:(x[0]), reverse=True)
    # print(answer)
    if not answer:
        result = '(None)'
    else:
        result = answer[0][1]
    return result