import sys
import math

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    S = input().strip()

    pos = [i for i, ch in enumerate(S) if ch == '1']  # 0-based
    m = len(pos)

    if m == 0:
        print("0/1")
        continue

    # Tính L[i]
    L = [0] * m
    l = 0
    for i in range(m):
        while l < m and pos[i] - pos[l] > K:
            l += 1
        L[i] = l

    # Tính R[i]
    R = [0] * m
    r = 0
    for i in range(m):
        while r + 1 < m and pos[r + 1] - pos[i] <= K:
            r += 1
        R[i] = r

    total = 0
    for i in range(m):
        total += (R[i] - L[i] + 1)

    if total == 0:
        print("0/1")
    else:
        denom = N * N
        g = math.gcd(total, denom)
        print(f"{total // g}/{denom // g}")
