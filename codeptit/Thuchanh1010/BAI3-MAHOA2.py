P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."  
while True:
    s = input()
    if s[0] == '0': break
    k, tmp = s.split()
    k = int(k)
    res = "" 
    for i in tmp:
        res += P[(P.index(i) + k) % 28]
    print(res[::-1])
