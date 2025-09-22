# Chữ số nguyên tố
import math

prime = {'2', '3', '5', '7'}

def snt(n):
    if n < 2:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    s = input().strip()
    cntPrime = 0
    cntNPrime = 0
    for i in range(0, len(s)):
        if s[i] == '2' or s[i] == '3' or s[i] == '5' or s[i] == '7':
            cntPrime += 1
        else:
            cntNPrime += 1
    if snt(len(s)) and cntPrime > cntNPrime:
        print("YES")
    else:
        print("NO")