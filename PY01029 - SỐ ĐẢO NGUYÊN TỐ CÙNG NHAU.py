import math

t = int(input())
for _ in range(t):
    n = input().strip()
    nn = n[::-1]
    if (math.gcd(int(n), int(nn))) == 1:
        print('YES')
    else:
        print('NO')
