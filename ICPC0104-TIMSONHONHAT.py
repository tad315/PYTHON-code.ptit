for _ in range(int(input())):
    s = input().strip()
    res = []
    tmp = 0
    for i in s:
        if i.isdigit(): 
            tmp = int(i) + tmp * 10
        else:
            if tmp > 0: 
                res.append(tmp)
                tmp = 0
    if tmp: 
        res.append(tmp)
    print(min(res))
