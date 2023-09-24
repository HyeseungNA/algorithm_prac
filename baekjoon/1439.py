# 예외 상황

s = input()

arr_1 = s.split('1')
arr_0 = s.split('0')

cnt_0 = 0
cnt_1 = 0

for i in range(len(arr_1)):
    if '0' in arr_1[i]:
        cnt_0 += 1
    
for i in range(len(arr_0)):
    if '1' in arr_0[i]:
        cnt_1 += 1
    
print(min(cnt_0,cnt_1))