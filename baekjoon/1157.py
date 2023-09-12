sentence = input()
sen = sentence.upper()

# 박스 안에 넣기
v = [0] * 26

for s in sen:
    v[ord(s) - 65] += 1

Max = 0
idx = 0
for i in range(26):
    if v[i] > Max:
        Max = v[i]
        idx = i


if v.count(Max) > 1:
    print('?')

else:
    print(chr(idx + 65))

