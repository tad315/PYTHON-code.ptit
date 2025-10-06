def isPrime(n):
    if n < 2: return False
    if n == 2: return True
    elif n % 2 == 0: return False
    for i in range (3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

n, m = map(int, input().split())
a = []
for _ in range(n):
    row = list(map(int, input().split()))
    
    nrow = [1 if isPrime(x) else 0 for x in row]
    a.append(nrow)

for row in a:
    print(" ".join(map(str, row)))