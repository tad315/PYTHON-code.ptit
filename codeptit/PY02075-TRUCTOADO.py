import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    segments = []

    for _ in range(n):
        x1, x2 = map(int, input().split())
        segments.append((x1, x2))
    segments.sort(key=lambda seg: seg[1])

    if n == 0:
        print(0)
        continue
    count = 1
    last_end = segments[0][1]
    for i in range(1, n):
        start, end = segments[i]
        if start >= last_end:    
            count += 1
            last_end = end

    print(count)
