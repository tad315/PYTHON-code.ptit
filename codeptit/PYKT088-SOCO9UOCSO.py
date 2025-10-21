def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    elif n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

nt = []
for i in range(2, 32000):
    if is_prime(i):
        nt.append(i)

n = int(input())
cnt = 0
for i in range(0, len(nt)):
    for j in range(i + 1, len(nt)):
        if nt[i] ** 2 * nt[j] ** 2 < n:
            cnt += 1
        else: 
            break
tmp = int(n**(1/8))
for i in nt:
    if i <= tmp:
        cnt += 1
print(cnt)