#Kiểm tra số đẹp
def check(s):
    if len(set(s)) != 2:
        return False
    for i in range(2, len(s)):
        if s[i] != s[i - 2]:
            return False
    return True

t = int(input())
for _ in range(t):
    s = input().strip()
    if check(s):
        print("YES")
    else:
        print("NO")
