for _ in range (int(input())):
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    mx = max(a)
    idx = a.index(mx)
    a.insert(idx, m)
    neg = [x for x in a if x < 0]
    nonneg = [x for x in a if x >= 0]
    print(*(neg + nonneg))