n = int(input())
a = [input().strip() for _ in range(n)]
ans = 0
for row in a: 
    r = row.count('C')
    ans += r * (r - 1) // 2
for col in range (n):
    c = sum(a[i][col] == 'C' for i in range(n))
    ans += c * (c - 1) // 2
print(ans)