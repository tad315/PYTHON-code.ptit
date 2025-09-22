n = int(input())
a = []
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
k = int(input())
sumT, sumB = 0, 0
for i in range(n):
    for j in range(n):
        if j < n - i - 1:
            sumT += a[i][j]
        elif j > n - i - 1:
            sumB += a[i][j]
k1 = abs(sumT - sumB)
if k >= k1: print("YES")
else: print("NO")
print(k1)