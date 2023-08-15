# from collections import Counter

# def solution(participant,completion):

#     answer = Counter(participant) - Counter(completion)
#     print(list(answer.keys())[0])
#     return
# solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])


def solution(participants,completion):
    # 참가자 딕셔너리
    answer = Counter(participants)
    
    for com in completion:
        if com in answer:
            answer[com] -= 1
    
    for key in answer:
        if answer[key] >= 1:
            return key 

