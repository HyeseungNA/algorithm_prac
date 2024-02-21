import sys

n,s = map(int, input().split())
numbers = list(map(int, input().split()))

left, right = 0, 0 # 두 개의 포인터는 0에서 부터 시작
sum = 0 # 합을 저장할 변수
min_length = sys.maxsize # 먼저 최대 길이로 지정

while True:
    if sum >= s:
        min_length = min(min_length, right - left)
        sum -= numbers[left]
        left += 1

    elif right == n or left == n:
        break
    
    else:
        sum += numbers[right]
        right += 1



if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)