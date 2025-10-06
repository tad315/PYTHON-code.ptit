for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    stack = []
    res = [0] * n
    for i in range(n):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        if not stack:
            res[i] = i + 1
        else:
            res[i] = i - stack[-1]
        stack.append(i)
    print(*res)