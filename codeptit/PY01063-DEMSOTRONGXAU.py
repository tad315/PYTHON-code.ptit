def cntN(s, n):
    n = str(n)
    cnt = 0
    pos = 0
    while True:
        idx = s.find(n, pos)
        if idx == -1: break
        cnt += 1
        pos = idx + len(n)
    return cnt

for _ in range(int(input())):
    s = input().strip()
    n = input().strip()
    print(cntN(s, n))