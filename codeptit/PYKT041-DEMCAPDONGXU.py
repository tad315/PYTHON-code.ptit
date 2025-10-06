n = int(input().strip())
a = [input().strip() for _ in range(n)]
res = 0
for i in range(n):
    cnt = a[i].count('C')
    res += cnt * (cnt - 1) // 2
for j in range (n):
    cnt = sum(1 for i in range(n) if a[i][j] == 'C')
    res += cnt * (cnt - 1) // 2
print(res)