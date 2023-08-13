def solution(k, tangerine):
    dic = dict()

    # dic 안에 다 넣기
    for i in range(len(tangerine)):
        if tangerine[i] in dic:
            dic[tangerine[i]] += 1
        else:
            dic[tangerine[i]] = 1
    
    sorted_dic = dict(sorted(dic.items(),key=lambda item:item[1],reverse=True))
    answer = 0
    # 딕셔너리를 돌면서 total 비교하기 
    for key in sorted_dic:
        k -= sorted_dic[key]
        answer += 1

        if k <= 0:
            break

    return answer
solution(6,[1, 3, 2, 5, 4, 5, 2, 3])