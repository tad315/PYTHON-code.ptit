def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    elif n % 2 == 0: return False
    for i in range(3, int(n ** 0.5 + 1), 2):
        if n % i == 0: return False
    return True

n = int(input())
a = list(map(int, input().split()))
b = []
for x in a:
    if x not in b:
        b.append(x)
ok = False
for i in range(len(b)):
    sum1 = sum(b[j] for j in range(0, i + 1))
    sum2 = sum(b[j] for j in range(i + 1, len(b)))
    if is_prime(sum1) and is_prime(sum2):
        print(i)
        ok = True
        break
if not ok: print('NOT FOUND')