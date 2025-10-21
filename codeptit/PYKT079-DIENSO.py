for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    L = min(a)
    R = max(a)
    cnt = 0
    for i in range(L, R + 1):
        if i not in a:
            cnt += 1
    print(cnt)