def solution(s):
    answer = []
    cnt1 = 0
    cnt2 = 0
    while True:
        cnt1 += 1
        tmp = []
        # 1의 개수
        c = s.count("1")
        # 0의 개수
        zero = s.count("0")
        cnt2 += zero
        
        if c == 1:
            answer.append(cnt1)
            answer.append(cnt2)
            break
        # 1의 개수를 2로 나눈 나머지를 tmp에 넣어주기
        while True:
             # 몫이 1이면 몫도 tmp에 넣어주기
            if c == 1:
                tmp.append(1)
                break
            tmp.append(c % 2)
            c = c // 2
       
        # 거꾸로 만들어주기
        tmp.reverse()
        s = "".join(map(str,tmp))
        print(s)


    
        
    return answer
solution("110010101001")