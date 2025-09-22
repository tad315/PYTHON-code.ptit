def sumDigits(n):
    return sum(int(d) for d in str(n))

for _ in range(int(input().strip())):
    n = int(input().strip())
    a = list(map(int, input().split()))
    a.sort(key=lambda x: (sumDigits(x), x))
    print(" ".join(map(str, a)))
