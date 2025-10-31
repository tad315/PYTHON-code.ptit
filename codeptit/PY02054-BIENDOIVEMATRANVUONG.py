n, m = map(int, input().split())
mt = [list(map(int, input().split())) for _ in range(n)]
if n > m:
    remove = []
    cnt = n - m
    for i in range(n):
        if (i + 1) & 1 and cnt > 0:
            remove.append(i)
            cnt -= 1
    mt = [row for i, row in enumerate(mt) if i not in remove]

elif n < m:
    remove = []
    cnt = m - n
    for j in range(m):
        if (j + 1) % 2 == 0 and cnt > 0:
            remove.append(j)
            cnt -= 1
    mt = [[val for j, val in enumerate(row) if j not in remove] for row in mt]
    
for row in mt:
    print(*row)