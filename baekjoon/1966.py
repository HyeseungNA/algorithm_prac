from collections import deque
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    numbers = list(map(int,input().split()))
    q = deque(enumerate(numbers))# 인덱스, 요소 순
    cnt = 0
    while q:
        nums = q.popleft()
        now_idx = nums[0]
        now_num = nums[1]

        for num in q:
            if num[1] > now_num:
                q.append((now_idx,now_num))
                break
        else:
            cnt += 1
            if now_idx == m:
                print(cnt)



    
    
    
