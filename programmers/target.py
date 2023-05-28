def solution(numbers,target):
    answer = 0
    def dfs(now, total):
        nonlocal answer
        if now >= len(numbers) : # numbers 길이와 같을 때 
            if total == target: # Total 값과 같을 때
                answer += 1  # count += 1
            return 
    

        dfs(now+1, total + numbers[now]) # 포함 할때
        dfs(now + 1 , total - numbers[now]) # 포함 안할 때 
    dfs(0,0)  #시작점, 합계, 카운트
    
    return answer
