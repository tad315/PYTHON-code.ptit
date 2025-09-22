t = int(input().strip())
for _ in range(t):
    expr = input().strip()
    stack = []
    res = []
    cnt = 0
    for c in expr:
        if c == '(':
            cnt += 1
            stack.append(cnt)
            res.append(str(cnt))
        elif c == ')':
            res.append(str(stack.pop()))
    print(' '.join(res))