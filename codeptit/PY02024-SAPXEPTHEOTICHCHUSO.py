def mulDigits(n):
    res = 1
    for d in str(n):
        res *= int(d)
    return res

for _ in range(int(input().strip())):
    n = int(input().strip())
    a = list(map(int, input().split()))
    a.sort(key=lambda x: (mulDigits(x), x))
    print(" ".join(map(str, a)))
