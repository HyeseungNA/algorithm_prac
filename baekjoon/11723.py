import sys
n = int(sys.stdin.readline())
answers = set()
for _ in range(n):
    # 명령
    order = sys.stdin.readline().strip().split()
    if len(order) == 1:
        if order[0] == 'all':
            answers = set(range(1,21))
        elif order[0] == 'empty':
            answers.clear()
    
    else:
        cmd = order[0]
        target = int(order[1])
        if cmd == 'add':
            answers.add(target)
        elif cmd == 'remove':
            answers.discard(target)
        elif cmd == 'check':
            print(1 if target in answers else 0)
        elif cmd == 'toggle':
            if target in answers:
                answers.discard(target)
            else:
                answers.add(target)


