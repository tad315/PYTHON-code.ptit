mod = 10**9 + 7
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    res = 0
    i = 0
    while k:
        if k & 1:
            res += pow(n, i, mod)
            res %= mod
        k >>= 1
        i += 1
    print(res)