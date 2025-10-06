# Số tăng giảm

def check (s):
    if len(s) < 3: return False
    i = 0
    n = len(s)
    while i < n and int(s[i]) < int(s[i + 1]): i += 1
    if i == 0 or i == n - 1: return False
    while i + 1 < n and int(s[i]) > int(s[i + 1]): i += 1
    return i == n - 1

for _ in range(int(input())):
    s = input().strip()
    if check(s): print("YES")
    else: print("NO")