g,s = map(int,input().split())
w = input()
S = input()

w_lst = [0] * 58
s_lst = [0] * 58

for char in w:
    w_lst[ord(char)- 65 ] += 1


st = 0
length = 0
cnt = 0
for i in range(s):
    s_lst[ord(S[i]) - 65] += 1
    length += 1

    if length == g:
        if s_lst == w_lst:
            cnt += 1

        length -= 1 
        s_lst[ord(S[st]) - 65] -= 1
        st += 1

print(cnt)

