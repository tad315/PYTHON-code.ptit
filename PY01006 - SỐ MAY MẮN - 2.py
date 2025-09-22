t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    ok = True
    for i in range(n):
        if s[i] != '4' and s[i] != '7':
            ok = False
            break
        else:
            ok = True
    if ok:
        print("YES")
    else:
        print("NO")
