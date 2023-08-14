def solution(participant, completion):
    answer = ''
    # 참가자 딕셔너리에 넣기
    par = dict()
    for i in range(len(participant)):
        if participant[i] not in par:
            par[participant[i]] = 1
        else:
            par[participant[i]] += 1


    # 완주자 돌면서
    for key in completion:
        # 참가자 리스트에 있으면
        if key in par:
            # 카운트 빼주기
            par[key] -= 1
    # 참가자 value가 1인 key 뽑기
    for key in par:
        if par[key] >= 1:
            answer = key

    return answer

solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])