import sys
from collections import deque

input = sys.stdin.readline

INF = 10**9

def min_steps(A, N, M):
    # dùng 0-index trong code
    dist = [[INF] * M for _ in range(N)]
    q = deque()

    dist[0][0] = 0
    q.append((0, 0))

    while q:
        i, j = q.popleft()
        dcur = dist[i][j]

        # nếu đã tới đích rồi thì có thể return luôn (tối ưu nhẹ)
        if i == N - 1 and j == M - 1:
            return dcur

        # đi xuống
        if i + 1 < N:
            step = abs(A[i][j] - A[i + 1][j])
            if step > 0:
                ni = i + step
                if ni < N and dist[ni][j] > dcur + 1:
                    dist[ni][j] = dcur + 1
                    q.append((ni, j))

        # đi sang phải
        if j + 1 < M:
            step = abs(A[i][j] - A[i][j + 1])
            if step > 0:
                nj = j + step
                if nj < M and dist[i][nj] > dcur + 1:
                    dist[i][nj] = dcur + 1
                    q.append((i, nj))

        # đi chéo xuống phải
        if i + 1 < N and j + 1 < M:
            step = abs(A[i][j] - A[i + 1][j + 1])
            if step > 0:
                ni = i + step
                nj = j + step
                if ni < N and nj < M and dist[ni][nj] > dcur + 1:
                    dist[ni][nj] = dcur + 1
                    q.append((ni, nj))

    return -1 if dist[N - 1][M - 1] == INF else dist[N - 1][M - 1]


T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = min_steps(A, N, M)
    print(ans)
