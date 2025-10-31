def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    elif n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = -1
for i in range(n):
    for j in range(m):
        if is_prime(a[i][j]):
            ans = max(ans, a[i][j])
if ans == -1:
    print("NOT FOUND")
else:
    print(ans)
    for i in range(n):
        for j in range(m):
            if a[i][j] == ans:
                print(f"Vi tri [{i}][{j}]")