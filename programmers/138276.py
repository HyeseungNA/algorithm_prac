def solution(k,tangerine):
    # 카운트
    answer = 0
    # 딕셔너리 만들고 요소들 넣기
    dic = dict()
    for i in range(len(tangerine)):
        if tangerine[i] not in dic:
            dic[tangerine[i]] = 1
        else:
            dic[tangerine[i]] += 1
        
    # 내림차순 정렬하기
    re_dict = dict(sorted(dic.items(),key=lambda x:x[1],reverse=True))
    # print(re_dict)

    for value in re_dict.values():
        # 현재 값에서 빼주기
        k -= value
        answer += 1
        # 현재 값이 0보다 작으면 멈추기
        if k <= 0:
            break
    return answer
