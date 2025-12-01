inf = 10**9
t = int(input())
for _ in range(t):
    n = int(input())
    x, y, z = map(int, input().split())
    dp = [inf] * (n + 1)
    dp[0] = 0
    dp[1] = x
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + x
        for j in range(1, i):
            if 2 * j >= i:
                cost = dp[j] + z + (2 * j - i) * y
                dp[i] = min(dp[i], cost)
    print(dp[n])