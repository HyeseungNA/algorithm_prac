def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = [0]

    for i in range(1, n):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)

    for i in range(0, len(stack) - 1):
        answer[stack[i]] = n - 1 - stack[i]

    return answer
