from collections import deque
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        copy = deque(skill)
        flag = 1
        for t in tree:
            while copy:
                if copy[0] == t:
                    copy.popleft()
                else:
                    for c in copy:
                        if c == t:
                            flag = 0
                            break
                    break
        if flag == 1:
            answer += 1

    return answer