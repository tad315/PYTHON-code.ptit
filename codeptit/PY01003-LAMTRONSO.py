for _ in range (int(input())):
    n = int(input())
    m = 10
    while m <= n:
        if (n % m) >= (m / 2):
            n = (n // m + 1) * m
        else: n = (n // m) * m
        m *= 10
    print(n)
            