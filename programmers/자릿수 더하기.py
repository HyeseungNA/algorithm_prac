def solution(n):
    answer = 0
    while n > 0:
        num = n % 10 
        answer += num
        print(answer)
        n = n // 10
    return answer
solution(125)