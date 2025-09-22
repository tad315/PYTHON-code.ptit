t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    ok = True
    for i in range(n - 1):
        if s[i] > s[i + 1]:
            ok = False
            break
    if ok:
        print ('YES')
    else: 
        print('NO')
