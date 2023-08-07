def solution(people,limit):
    answer = 0
    people.sort()

    now = 0
    new = len(people) - 1

    while now <= new:

        if people[now] + people[new] > limit:
            new -= 1
            answer += 1
        else:
            now += 1
            new -= 1
            answer += 1

    return answer

    
solution([70,50,80,50],100)