n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

max_val = max(max(row) for row in a)
min_val = min(min(row) for row in a)
mm = max_val - min_val

pos = []
for i in range(n):
    for j in range(m):
        if a[i][j] == mm:
            pos.append((i, j))
if not pos: 
    print("NOT FOUND")
else:
    print(mm)
    for i, j in pos:
        print(f"Vi tri [{i}][{j}]")
        