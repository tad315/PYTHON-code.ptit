def getSum(s):
    return sum(int(i) for i in s)

def check(s):
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != 2: return False
    return True

for _ in range(int(input())):
    s = input()
    if getSum(s) % 10 == 0 and check(s): print("YES")
    else: print("NO")