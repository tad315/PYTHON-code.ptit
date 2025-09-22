def snt(n):
    if n < 2: return False
    if n == 2: return True
    elif n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

def cnt(n):
    cnt = 0
    for i in n:
        if i in '2357': cnt += 1
        
    return cnt > len(n) - cnt

for _ in range(int(input())):
    n = input()
    if snt(len(n)) and cnt(n): print("YES")
    else: print("NO")