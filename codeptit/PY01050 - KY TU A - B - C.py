def backTrack (cur, n, a, b, c):
    if a <= b <= c and a > 0 and len(cur) == n:
        print(cur)
    if len(cur) < n:
        backTrack(cur + 'A', n, a + 1, b, c)
        backTrack(cur + 'B', n, a, b + 1, c)
        backTrack(cur + 'C', n, a, b, c + 1)
n = int(input().strip())
for i in range(3, n + 1):
    backTrack("", i, 0, 0, 0)