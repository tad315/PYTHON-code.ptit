# Số thuận nghịch chẵn

from itertools import product


def generate(limit):
    d = ['0', '2', '4', '6', '8']
    res = []
    n = len(str(limit))
    for l in [2, 4, 6]:
        if l > n: continue
        halfL = l // 2
        for half in product(d, repeat=halfL):
           if half[0] == '0': continue
           left = ''.join(half)
           num = int(left + left[::-1])
           if num < limit: res.append(num)
    return sorted(res)

for _ in range(int(input())):
    n = int(input())
    ans = generate(n)
    print(*ans)