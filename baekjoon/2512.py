#이분탐색으로 풀면 될듯
# 빼서 더한 총 값이 예산보다 작아질때까지

def binary(start,end):
    total = 0
    # mid = 상한액
    mid = (start + end + 1) //2
    # 시작값이 끝 값보다 크거나 같을 때 멈춰

    if start >= end:
        return mid
    
    # 총합 계산
    for i in range(len(costs)):
        # 상한액보다 더 높으면 가격을 상한액으로
        if costs[i] >= mid:
            total += mid
            continue
        total += costs[i]
    # 총합이 예산보다 작으면
    # 시작점을 mid보다 크게
    if total < money:
        start = mid
        return binary(start, end)
  

    # 총합이 예산보다 크면
    # 끝점을 mid보다 작게
    if total > money:
        end = mid - 1
        return binary(start, end)

    # 총합이랑 같으면 바로 상한액 return 시켜버리기
    if total == money:
        return mid



n = int(input())
costs = list(map(int,input().split()))
money = int(input())

result = binary(1, max(costs))
print(result)