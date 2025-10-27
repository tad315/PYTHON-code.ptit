for _ in range (int(input())):
    n, m, k = map(int, input().split())
    a = []
    b = []
    c = []
    while len(a) < n:
        a.extend(map(int, input().split()))
    while len(b) < m:
        b.extend(map(int, input().split()))
    while len(c) < k:
        c.extend(map(int, input().split()))
        
    i = j = l = 0
    res = []
    
    while i < n and j < m and l < k:
        if a[i] == b[j] == c[l]:
            res.append(a[i])
            i += 1
            j += 1
            l += 1
        else:
            mn = min(a[i], b[j], c[l])
            if a[i] == mn: i += 1
            if b[j] == mn: j += 1
            if c[l] == mn: l += 1
    if res: print(*res)
    else: print("NO")