def snt(n):
    if n < 2: return False
    if n == 2: return True
    elif n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

def check(n):
    if snt(int(n[:3])) and snt(int(n[-3:])): return True
    return False

for _ in range(int(input())):
    n = input()
    if check(n): print("YES")
    else: print("NO")