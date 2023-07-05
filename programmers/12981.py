def solution(n,words):
    answer = []
    st = []


    for i in range(len(words)):
        print(st,'____')
        if not st:
            st.append(words[i])
            continue
            print(st)
            print(st[-1][-1])
        # st 마지막 값 끝 값과 단어 앞 글자가 같으면
        if st[-1][-1] == words[i][0]:

            #스택에 없으면 스택에 넣어주기
            if words[i] not in st:
                st.append(words[i])
                continue
                print(st)
            # 만약 스택에 이미 있다면
            else:

                # 턴 구하기
                turn = (i / n) + 1
                # 번호 구하기
                num = (i % n) + 1
                answer.append(turn)
                answer.append(num)
                break
        elif st[-1][-1] != words[i][0]:
            turn = (i / n) + 1
            num = (i % n) + 1
            answer.append(turn)
            answer.append(num)
            break
                
    if len(st) == len(words):
        answer = [0,0]
        
    

        

            
    return answer