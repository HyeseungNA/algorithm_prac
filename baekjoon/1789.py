# 총 합이 s보다 크면 오른쪽으로 이동
# 시작이 s보다 크면 멈춰

s = int(input())
total = 0
cnt = 0
num = 0
while True:
    num += 1
    total += num
    cnt += 1
    if total == s:
        print(cnt)
        break

    if total > s:
        print(cnt-1)
        break




