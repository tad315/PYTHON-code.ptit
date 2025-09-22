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

t = int(input())
for _ in range(t):
    n = input()
    if snt(getSum(n)):
        print("YES")
    else: 
        print("NO")