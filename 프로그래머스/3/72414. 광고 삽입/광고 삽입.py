def get_seconds(time):
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s


def get_h_m_s(answer):
    return "{:02d}:{:02d}:{:02d}".format(answer // 3600, (answer % 3600) // 60, answer % 60)


def solution(play_time, adv_time, logs):
    play_time, adv_time = get_seconds(play_time), get_seconds(adv_time)
    max_time = 0
    times = [0] * (play_time + 1)  # 수정된 부분
    answer = 0

    for log in logs:
        start, end = log.split('-')
        st = get_seconds(start)
        ed = get_seconds(end)
        
        times[st] += 1
        times[ed] -= 1

    for i in range(1, play_time):
        times[i] += times[i - 1]

    for i in range(1, play_time):
        times[i] += times[i - 1]

    for i in range(play_time):
        if i < adv_time - 1:
            if max_time < times[i]:
                max_time = times[i]
                answer = 0
        else:
            if max_time < times[i] - times[i - adv_time]:
                max_time = times[i] - times[i - adv_time]
                answer = i - adv_time + 1

    return get_h_m_s(answer)
