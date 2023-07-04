def solution(s):
    answer = -1
    st = []


    for i in range(len(s)):

        # 스택이 비어있다면 스택에 넣어라
        if not st:
            st.append(s[i])

        else:
            if st[-1] == s[i]:
                st.pop()
            else:
                st.append(s[i])

    
    if not st:
        answer = 1
    else:
        answer = 0
    return answer
    