for _ in range(int(input().strip())):
    s = input().strip()
    res = []
    sum = 0
    for x in s:
        if x.isdigit():
            sum += int(x)
        else:
            res.append(x)
    res.sort()
    res.append(str(sum))
    print(*res, sep='')