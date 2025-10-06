n = int(input())
a = []
if (len(a) < n):
    while len(a) < n:
        k = input().split()
        for x in k: a.append(int(x))
chan = sorted([x for x in a if x % 2 == 0])
le = sorted([x for x in a if x & 1], reverse = True)
c, l = 0, 0
for i in range(n):
    if a[i] % 2 == 0:
        a[i] = chan[c]
        c += 1
    else:
        a[i] = le[l]
        l += 1
print(*a)