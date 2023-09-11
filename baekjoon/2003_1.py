n,m = map(int,input().split())
numbers = list(map(int,input().split()))

left = 0
right = left + 1
cnt = 0
while left <= n-1 and right<= n and left < right:
    # 총합
    total = sum(numbers[left:right])
    # 총합이 m 보다 작으면 오른쪽으로 이동
    if total < m:
        right += 1
    # 총합이 m이랑 같으면 cnt 더해주고, total 초기화, left 이동
    elif total == m:
        cnt += 1
        total = 0
        left += 1
        right = left + 1
    # 총합이 m보다 크면 total 초기화, left 이동
    else:
        total = 0
        left += 1
        right = left + 1
print(cnt)
