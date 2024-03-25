import heapq
def solution(n, t, m, timetable):
    heap = []
    for time in timetable:
        #도착한 순서대로 큐에 넣어놓기
        hour, min = time.split(':')
        time = int(hour) * 60 + int(min)
        heapq.heappush(heap,time)
    answer = ''
    arrive = 9 * 60 + 0 # 처음 도착
    print(arrive)
    print(heap)


    while n > 1: # 마지막 기회 전까지는 마음 편하게 있기,,
        person = m # 태울 수 있는 사람 수
        while heap:
            now = heapq.heappop(heap)
            if person > 0 and now <= arrive: # 태울 자리가 있고, 도착 시간보다 빨리 서있었다면
                person -= 1
            else: # 태울 자리가 없거나 도착시간보다 늦었으면
                heapq.heappush(heap,now)
                arrive += t # 버스 떠나기
                n -= 1
                break

    print(heap)  
    while m > 1: # 한 자리 남을 때까지는
        if heap:
            now = heapq.heappop(heap)
            if now <= arrive:
                m -= 1
            else:
                heapq.heappush(heap,now)
                break
 
    if heap:
        now = heapq.heappop(heap)
        if arrive >= now:
            answer = now - 1
        else:
            answer = arrive

    else:
        answer = arrive
    
    ho = answer // 60
    mi = answer % 60
    
    print(f'{ho:02d}:{mi:02d}')
    return answer

solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])