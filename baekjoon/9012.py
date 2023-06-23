n = int(input())
for _ in range(n):
    word = list(input())
    st = []
    # 스택에 넣어주기
    for i in range(len(word)):
        if len(st) == 0:
            st.append(word[i])
         # 스택에 (이 있고 배열에 )이 있으면 스택에서 빼주기 
        elif st[-1] == '(' and word[i] == ')':
            st.pop()
        else:
            st.append(word[i])

       


    # 배열 다 돌았는데도 스택에 남아있으면 no
    if len(st) != 0:
        print('NO')
    else:
        # 아니면 yees
        print('YES')

