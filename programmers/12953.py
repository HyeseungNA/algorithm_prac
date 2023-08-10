def solution(arr):
    # 최소 구하기
    Min = max(arr)
    while True:
        cnt = 0

        for num in arr:
            if Min % num == 0:
                cnt += 1
            else:
                Min += 1
        if cnt == len(arr):
            break



    return Min