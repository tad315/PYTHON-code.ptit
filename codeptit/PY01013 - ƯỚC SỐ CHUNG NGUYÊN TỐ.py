import math

def snt(n):
    if n < 2:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    g = math.gcd(a, b)
    tong = sum(int(c) for c in str(g))
    if snt(tong):
        print('YES')
    else: 
        print('NO')
