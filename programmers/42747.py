def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    answer = 0
    # 논문을 돌면서
    for i in range(1,n+1):
        # 순위가 더 작거나 같으면 answer값 업데이트
        if i <= citations[i-1]:
            answer = i
            
    return answer
result = solution([3,3,3])
print(result)