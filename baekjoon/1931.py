n = int(input())
hour = []

for _ in range(n):
    hour.append(list(map(int, input().split())))

hour = sorted(hour, key=lambda x: (x[1], x[0]))


ed = hour[0][1]
cnt = 1
for i in range(1,n):
    # 회의실 시작 시간
    st = hour[i][0]
    # 시작 시간이 회의 끝나는 시간이랑 같거나 늦을 때만
    if st >= ed:
        ed = hour[i][1] # 끝나는 시간 바꿔주고
        cnt += 1 # 이용 횟수 추가

print(cnt)
    
