n = int(input())
a = [list(map(int, input().split())) for _ in range(n)] 
k = int(input())
sumT = sum(a[i][j] for i in range(n) for j in range(n) if i < j)
sumB = sum(a[i][j] for i in range(n) for j in range(n) if i > j)
print('YES' if abs(sumT - sumB) <= k else 'NO')
print(abs(sumT - sumB))

