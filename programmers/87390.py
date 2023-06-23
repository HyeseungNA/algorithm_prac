def solution(n,left,right):
    answer = []
    for i in range(left,right + 1):
        # 2차원 배열을 1차원으로 한꺼번에 만들기
        a = i // n
        b = i % n
        answer.append(max(a,b) + 1)
    return answer
