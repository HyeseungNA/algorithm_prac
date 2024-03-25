n,c = map(int,input().split())
house = []
for _ in range(n):
    house.append(int(input()))

house.sort()
answer = 0
st = 1 # 최소 거리
ed = house[-1] - house[0] # 최대거리

while st <= ed:
    tmp = float("INF")
    cnt = 1
    now = house[0] # 공유기 설치
    mid = (st + ed) // 2

    for i in range(1,n):
        if now + mid <= house[i]:
            cnt += 1
            tmp = min(house[i] - now, tmp)
            now = house[i]
    
    if cnt < c: # 공유기 설치를 더 해야함 -> 간격을 짧게 해야 함
        ed = mid - 1

    elif cnt >= c: # 공유기 설치가 완료 or 더 많이 됨 -> 간격 늘려야 함
        st = mid + 1
        answer = max(answer, tmp)
    

print(answer)

'''
9 3

1 2 3 4 5 6 7 8 100

'''