# 스택으로 풀기

def solution(s):
    tmp = list(s)
    answer = 0
    for _ in range(len(s)):
        st = []
        for i in range(len(tmp)):
            if len(st) > 0:
                if st[-1] == '[' and tmp[i] == ']':
                    st.pop()
                
                elif st[-1] == '{' and tmp[i] == '}':
                    st.pop()
                
                elif st[-1] == '(' and tmp[i] == ')':
                    st.pop()
                else:
                    st.append(tmp[i])
            else:
                st.append(tmp[i])
        if len(st) == 0:
            answer += 1
        tmp.append(tmp.pop(0))
    return answer

