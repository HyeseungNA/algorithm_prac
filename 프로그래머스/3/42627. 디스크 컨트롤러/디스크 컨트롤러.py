def solution(jobs):
    answer = 0
    now = 0 # 작업 완료 시간
    n = len(jobs) 
    jobs.sort(key=lambda x:x[0])
    while jobs:
        Min = int(12e8)
        idx = -1
        for i in range(len(jobs)):
            if jobs[i][0] <= now:
                if jobs[i][1] < Min:
                    Min = jobs[i][1]
                    idx = i
        if idx == -1:
            now = jobs[0][0]
        else:
            
            answer += now - jobs[idx][0] + Min
            now += Min
            jobs.pop(idx)
        
        
    
    return answer // n