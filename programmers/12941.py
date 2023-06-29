def solution(A,B):
    answer = 0
    # 오름차순 정렬
    A.sort()
    # 내림차순 정렬
    B.sort(reverse = True)
    

    # 누적해서 더해주기
    for i in range(len(A)):
        answer += (A[i] * B[i])
    
    return answer