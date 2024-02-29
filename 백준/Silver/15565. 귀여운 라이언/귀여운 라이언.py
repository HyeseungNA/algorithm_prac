import sys

n, k = map(int, sys.stdin.readline().split())       # k 이상 라이언, n 인형
arr = list(map(int, sys.stdin.readline().split()))  # 1은 라이언, 2는 어피치

result = int(1e9)  # 가장 작은 연속된 인형 집합 크기
cnt = 0          # 현재 포인터에서 라이언 인형 수

left = 0
right = 0
if arr[left] == 1:
    cnt += 1
while right < n:
    if cnt == k:
        result = min(result,right - left + 1)
        if arr[left] == 1:
            cnt -= 1
        if left < n:
            left += 1

    else:
        right += 1
        if right < n and arr[right] == 1:
            cnt += 1

if result == int(1e9):
    print(-1)
else:
    print(result)