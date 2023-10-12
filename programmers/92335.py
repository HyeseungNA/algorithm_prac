def solution(n, k):
    answer = 0
    # k진수 변환
    word = ''
    while n:
        word = str(n%k) + word
        n = n // k
    
    word = word.split('0')
#     print(word)
    
    
    for w in word:
        flag = 1
        if len(w) == 0:
            continue
        if int(w) == 1:
            continue
        else:
            for i in range(2,int(int(w) ** 0.5) + 1):
                if int(w) % i == 0:
                    flag = 0
        if flag == 1:
            answer += 1
                
    
    return answer