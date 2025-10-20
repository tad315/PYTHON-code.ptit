from math import gcd
for _ in range (int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    dp = {0: 0}
    b = [0]
    for i in range (n):
        for G in b:
            g = gcd(G, a[i])
            cost = dp[G] + c[i]
            if g not in dp:
                dp[g] = cost
                b.append(g)
            else: 
                dp[g] = min(dp[g], cost)
    print(dp[1] if 1 in dp else -1)