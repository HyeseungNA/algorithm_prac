sen = input()
answer = ''
for c in sen:
    if c >= 'a' and c <= 'm':
        answer += chr(ord(c) + 13)
    elif c > 'm' and c <= 'z':
        answer += chr(ord(c) - 13)
    elif c >= 'A' and c <= 'M':
        answer += chr(ord(c) + 13)
    elif c > 'M' and c <= 'Z':
        answer += chr(ord(c) - 13)
    else:
        answer += c

print(answer)
