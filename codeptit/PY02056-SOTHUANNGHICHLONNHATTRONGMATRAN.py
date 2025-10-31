def TN(n):
    s = str(n)
    return len(s) >= 2 and s == s[::-1]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = -1
for i in range(n):
    for j in range(m):
        if TN(a[i][j]):
            ans = max(ans, a[i][j])
if ans == -1:
    print("NOT FOUND")
else:
    print(ans)
    for i in range(n):
        for j in range(m):
            if a[i][j] == ans:
                print(f"Vi tri [{i}][{j}]")