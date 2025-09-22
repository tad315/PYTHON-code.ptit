def snt(n):
    if n < 2: return False
    if n == 2: return True
    elif n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

def getSum(s):
    sum = 0
    for i in s:
        sum += int(i)
    return sum

def check(n):
    for i in range(0, len(n)):
        if i % 2 == 0 and n[i] not in '02468': return False
        if i % 2 == 1 and n[i] not in '13579': return False
    if snt(getSum(n)): return True
    return False

for _ in range(int(input())):
    n = input()
    if check(n): print("YES")
    else: print("NO")    