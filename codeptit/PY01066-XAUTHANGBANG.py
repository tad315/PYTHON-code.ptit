def check(s):
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s[len(s) - i]) - ord(s[len(s) - i - 1])):
            return False
    return True

for _ in range(int(input())):
    s = input().strip()
    if check(s): print("YES")
    else: print("NO")