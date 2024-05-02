def solution(s):
    cnt1 = 0
    cnt2 = 0
    answer = 0
    for i in range(len(s)):
        if cnt1 == 0:
            now = s[i]
            cnt1 += 1
        else:
            if s[i] == now: # 연속적이면
                cnt1 += 1
            else: # 다른 글자 나오면
                cnt2 += 1
        
            if cnt1 == cnt2:
                answer += 1
                cnt1 = 0
                cnt2 = 0
    
    if cnt1 > 0:
        answer += 1
    return answer