def change(n, b, X):
    if b == 2: return X
    gr = {4: 2, 8: 3, 16: 4}[b]
    while len(X) % gr != 0:
        X = '0' + X
    digits = "0123456789ABCDEF"
    res = []
    for i in range(0, len(X), gr):
        tmp = X[i: i + gr]
        val = int(tmp, 2)
        res.append(digits[val])
    return "".join(res).lstrip('0') or '0'

with open("DATA.in") as fin, open("DATA.out", "w") as fout:
    for _ in range(int(fin.readline().strip())):
        b = int(fin.readline().strip())
        X = fin.readline().strip()
        if b == 2: 
            fout.write(X + "\n")
        else:
            n = int(X, 2)
            fout.write(change(n, b, X) + "\n")
