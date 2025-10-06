def snt(n):
    if n < 2: return False
    if n == 2: return True
    elif n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

for _ in range(int(input())):
    n = input()
    if snt(int(n[-4:])): print("YES")
    else: print("NO")