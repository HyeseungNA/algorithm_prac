from fractions import gcd

def solution(arr):
    answer = arr[0]

    for num in arr:
        answer = n * answer / gcd(n,answer)


    return answer