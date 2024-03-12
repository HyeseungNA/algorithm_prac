word = input()
result = ''
idx = 0
while True:
    if idx >= len(word):
        break
    result = word[idx:idx + 10]
    print(result)
    result = ''
    idx += 10


