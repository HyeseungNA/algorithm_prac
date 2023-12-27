def convert(num,n):
    
    if num == 0:
        return '0'
    
    numbers = '0123456789ABCDEF'
    tmp = ''
    while num > 0:
        num,mod = divmod(num,n)
        tmp += numbers[mod]

    return tmp[::-1]


def solution(n, t, m, p):
    answer = ''
    game = ''
    cnt = 0
    for i in range(t * m):
        game += convert(i,n)
    
    while True:
        if cnt == t:
            break
        
        answer += game[p-1]
        p += m
        cnt += 1
    return answer