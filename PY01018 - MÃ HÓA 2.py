P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    line = input().strip()
    if not line:
        continue
    pt = line.split()
    if len(pt) == 1:
        k = int(pt[0])
        if k == 0:
            break
        else:
            continue
    else:
        k, s = pt
        k = int(k)
        if k == 0:
            break
    res = ""
    s = s[::-1]
    for c in s:
        idx = P.index(c)
        res += P[(idx + k) % 28]
    print (res)
