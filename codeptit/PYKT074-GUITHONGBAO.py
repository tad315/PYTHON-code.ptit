for _ in range(int(input().strip())):
    s = input().strip()
    words = s.split()
    L = 0
    res = ""
    for w in words:
        if L + len(w) + (1 if L > 0 else 0) > 100:
            break
        if L > 0:
            res += " "
            L += 1
        res += w
        L += len(w)
    print(res)