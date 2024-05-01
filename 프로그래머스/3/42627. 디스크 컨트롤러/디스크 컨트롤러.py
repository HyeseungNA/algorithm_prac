def solution(jobs):
    answer = 0
    now = 0
    n = len(jobs)
    jobs.sort(key=lambda x: x[0])  # 요청 시간을 기준으로 작업을 정렬
    
    while jobs:
        Min = int(12e8)
        idx = -1
        for i in range(len(jobs)):
            if jobs[i][0] <= now:  # 현재 시간 이전에 요청된 작업일 때
                if jobs[i][1] < Min:  # 소요 시간이 가장 짧은 작업 선택
                    Min = jobs[i][1]
                    idx = i
        if idx == -1:  # 현재 시간 이전에 요청된 작업이 없을 때
            now = jobs[0][0]  # 다음 작업의 요청 시간으로 시간을 이동
        else:
            answer += now - jobs[idx][0] + Min
            now += Min
            jobs.pop(idx)
    
    return answer // n
