while True:
    sentence = input()
    if sentence == '.':
        break
    stack = []
    for sen in sentence:
        if sen == ")":
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif sen == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif sen == '(' or sen == '[':
            stack.append(sen)

    if stack:
        print('no')
    else:
        print('yes')
        