def snt(n):
    if n < 2: return False
    if n == 2: return True
    elif n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

def check(n):
    for i in range(0, len(n)):
        if snt(i):
            if n[i] not in '2357': return False
        else:
            if n[i] not in '014689': return False
    return True

for _ in range(int(input())):
    n = input()
    if check(n): print("YES")
    else: print("NO")