def gen(n, prev, cur, res):
    if n == 0:
        res.append('(' + " ".join(map(str, cur)) + ')')
        return
    for i in range(min(prev, n), 0, -1):
        gen(n - i, i, cur + [i], res)
for _ in range(int(input())):
    n = int(input())
    res = []
    gen(n, n, [], res)
    print(len(res))
    print(" ".join(res))