import math

def snt(n):
    if n < 2:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def nto_cn (n):
    cnt = 0;
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            cnt += 1
    return cnt

t = int(input())
for _ in range(t):
    n = int(input())
    k = nto_cn(n)
    if snt(k):
        print('YES')
    else:
        print('NO')
