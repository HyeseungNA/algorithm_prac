kro = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = input()
cnt = 0
for k in kro:
    while True:
        if k in word:
            word = word.replace(k,'|',1)
            cnt += 1
        if k not in word:
            break

for w in word:
    if w != '|':
        cnt += 1
print(cnt)