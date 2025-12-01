import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if n == 1:
        print("YES" if a[0] == k else "NO")
        continue

    g = 0
    base = a[0]
    for x in a[1:]:
        g = math.gcd(g, abs(x - base))

    if (k - base) % g == 0:
        print("YES")
    else:
        print("NO")
