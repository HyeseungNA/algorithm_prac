def solution(n):
    ans = 0

    # 나누어 떨어지는
    # 나머지가 1인

    while n > 0:

        # 나머지가 떨어지는
        if n % 2  == 0:
            n = n//2
        
        elif n % 2 == 1:
            ans += 1
            n = n //2


    return ans
solution(5)