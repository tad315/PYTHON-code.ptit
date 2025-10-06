# Kiểm tra hệ cơ số 3

def check (s):
    for i in range(len(s)):
        if s[i] not in {'0', '1', '2'}: return False

    return True

for _ in range(int(input())):
    s = input()
    if check(s): print("YES")
    else: print("NO")