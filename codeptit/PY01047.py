# Kiểm tra nguyên tố
import math

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
    if snt(int(s[-4:])):
        print("YES")
    else:
        print("NO")
