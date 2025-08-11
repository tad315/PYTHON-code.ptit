t = int(input())
for _ in range(t):
    n, x, m = map(float, input().split())
    ans = 0
    while n <= m:
        ans += 1
        n *= (x / 100) + 1
    print(ans)
