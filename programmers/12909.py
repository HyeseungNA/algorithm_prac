def solution(s):
    s = list(s)
    # 스택 만들기
    st = []
    answer = ''
    # 스택 마지막에 (가 있고 리스트에 )가 있으면 빼주기
    for i in range(len(s)):

        if not st:
            st.append(s[i])
            continue
        
        if st[-1] == '(' and s[i] == ')':
            st.pop(-1)
        elif st[-1]== '(' and s[i] == '(':
                st.append('(')
        
    if st:
        answer = False
    else:
        answer = True
    
    return answer
