s = input().strip()
while len(s) % 3 != 0:
    s = '0' + s
res = ''
for i in range(0, len(s), 3):
    gr = s[i : i + 3]
    res += str(int(gr, 2))
print(res.lstrip('0') or '0')