n,m = map(int,input().split())
house = []
for _ in range(n):
    house.append(int(input()))

house.sort()
st = 1
ed = house[-1] - house[0]

answer = 0

while st <= ed:
    mid = (st + ed) // 2 # 공유기 거리
    cnt = 1
    cur = house[0] # 현재 공유기 위치
    for i in range(1,n):
        if house[i] - cur >= mid: # 거리가 현재 공유기 거리보다 크면
            cur = house[i] # 공유기 설치
            cnt += 1
    
    if cnt >= m:
        st = mid + 1
        answer = max(answer,mid)
        
    else:
        ed = mid - 1

print(answer)   