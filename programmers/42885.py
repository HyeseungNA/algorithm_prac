def solution(people,limit):
    answer = 0
    people.sort()

    now = 0
    ne = len(people) - 1

    while now <= ne:

        if people[now] + people[ne] <= limit:
            now += 1
            ne -=1
            answer +=1
        else:
            ne -= 1
            answer +=1
    return answer
    
solution([70,50,80,50],100)