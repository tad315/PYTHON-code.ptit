n, k = map(int, input().split())
a = list(map(int, input().split()))
if n <= 1:
    print(0 if n == 0 else 1)
else:
    a.sort()
    res = 1
    for i in range(1, n):
        if a[i] - a[i - 1] > k:
            res += 1
    print(res)