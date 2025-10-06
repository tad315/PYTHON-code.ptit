import math

T = int(input().strip())
for _ in range(T):
    n, k = map(int, input().split())
    a = []
    while len(a) < n:
        list = input().split()
        for x in list: a.append(int(x))
    if k in a: print(1)
    else:
        ans = 1e10
        for i in range(n - 1):
            tmp = a[i]
            for j in range(i + 1, n):
                tmp = math.gcd(tmp, a[j])
                if tmp < k: break
                elif tmp == k:
                    ans = min(ans, j - i + 1)
                    break
        print(-1 if ans == 1e10 else ans)
