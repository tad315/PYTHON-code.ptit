m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

vis = [[0] * n for _ in range(m)]

res = 0

for i in range(m):
    for j in range(n):
        if a[i][j] == -1:
            for k in range (8):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < m and 0 <= nj < n and not vis[ni][nj]:
                    vis[ni][nj] = 1
                    res += a[ni][nj]
print(res)
