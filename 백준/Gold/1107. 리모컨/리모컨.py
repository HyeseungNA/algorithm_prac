n = int(input())
# 100부터 해당 번호까지 가는 횟수
ans = abs(100 - n)
m = int(input())
if m:
    broken = list(input().split())
else:
    broken = list()
 
# 갈 수 있는 모든 채널
for num in range(1000001):
    # 부서진 번호로 가려 한다면 break
    for N in str(num):
        if N in broken:
            break
    else:
        # 정답 갱신
        ans = min(ans, len(str(num)) + abs(num - n))
print(ans)
 