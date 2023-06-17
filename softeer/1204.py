n,b = map(int,input().split())
computers = list(map(int,input().split()))

start = min(computers) 
end = 10 ** 9

total = 0
while True:
    total = 0
    mid = (start + end + 1) // 2
    # start가 end보다 크면 멈추기
    if start > end:
        break
    for i in range(len(computers)):
        if mid > computers[i]:
            total += (mid - computers[i]) ** 2
    # 총합이 b보다 작으면 mid값보다 높게
    if total <= b:
        start = mid + 1
    # 총합이 b보다 크면 mid보다 낮게
    elif total > b:
        end = mid - 1
    # 총합이랑 b가 같으면 mid 출력하고 중지
    # else:
    #     break
pri