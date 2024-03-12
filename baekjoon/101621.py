n = int(input())
times = [300, 60, 10]
time = 0
st = 0
cnt = 0
result = [0] * 3
while time <= n and st < 3:
    time += times[st]
    cnt += 1
    if time == n:
        result[st] = cnt
        print(*result)
        break
    if time < n:
        continue
    
    if time > n:
        time -= times[st]
        cnt -= 1
        result[st] = cnt
        cnt = 0 
        st += 1
    
if time != n:
    print(-1)

    