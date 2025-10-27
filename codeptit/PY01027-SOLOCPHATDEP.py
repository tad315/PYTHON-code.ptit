def check(s):
    s = s.replace('888', '1')
    for c in s: 
        if c not in '68':
            return False
    return True

s = input()
if check(s):
    print("YES")
else:
    print("NO")
