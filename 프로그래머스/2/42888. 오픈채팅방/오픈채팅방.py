def solution(record):
    users = {}
    answer = []

    for re in record:
        parts = re.split(' ')
        order, user_id = parts[0], parts[1]

        if order == 'Enter' or order == 'Change':
            users[user_id] = parts[2]

    for re in record:
        parts = re.split(' ')
        order, user_id = parts[0], parts[1]

        if order == 'Enter':
            answer.append(f'{users[user_id]}님이 들어왔습니다.')
        elif order == 'Leave':
            answer.append(f'{users[user_id]}님이 나갔습니다.')

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
result = solution(record)
print(result)
