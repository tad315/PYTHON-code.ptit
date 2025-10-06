t = int(input())
for _ in range(t):
    n = int(input())
    res = ['1']
    d = 2
    while d * d <= n:
        if n % d == 0:
            cnt = 0
            while n % d == 0:
                n //= d
                cnt += 1
            res.append(f"{d}^{cnt}")
        d += 1
    if n > 1:
        res.append(f"{n}^1")
    print(" * ".join(res))
