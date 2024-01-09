from heapq import heappop, heappush
def solution(book_time):
    answer = 0
    times = []
    for st,ed in book_time:
        times.append([int(st[:2]) * 60 + int(st[3:]), int(ed[:2]) * 60 + int(ed[3:])])
    
    times.sort()
    
    heap = []
    
    for s,e in times:
        if not heap:
            heappush(heap,e)
            answer += 1
        else:
            
            if heap[0] <= s:
                heappop(heap)
                heappush(heap,e+10)
            else:
                answer += 1
                heappush(heap,e+10)
    
    return answer