def solution(n):
    answer = 0
    b = n + 1
    while True:

        # 2진수로 변한 숫자와 1의 개수가 같으면 끝내주기
        if bin(n).count('1') == bin(b).count('1'):
            answer =  b
            break
        b += 1


    return answer