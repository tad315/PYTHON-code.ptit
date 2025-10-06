a, k, n = map(int, input().split())
res = []
start = ((a // k) + 1) * k
for s in range(start, n + 1, k):
    b = s - a
    if b > 0:
        res.append(b)
        
if res:
    print(" ".join(map(str, res)))
else:
    print(-1)
