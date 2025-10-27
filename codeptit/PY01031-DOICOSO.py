def solve(n, b):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        res = digits[n % b] + res
        n //= b
    return res or "0"

for _ in range(int(input().strip())):
    n, b = map(int, input().split())
    print(solve(n, b))