def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    elif n % 2 == 0: return False
    for i in range(3, int(n ** 0.5 + 1), 2):
        if n % i == 0: return False
    return True

n = int(input())
a = list(map(int, input().split()))
b = [x for x in a if is_prime(x)]
b.sort()
i = 0
for x in a:
    if x not in b: print(x, end=' ')
    else:
        print(b[i], end=' ')
        i += 1