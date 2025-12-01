import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, banned, adj, N):
    q = deque([start])
    visited = [False] * (N + 1)
    if start == banned:
        return visited
    visited[start] = True

    while q:
        u = q.popleft()
        for v in adj[u]:
            if v == banned:
                continue
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return visited

T = int(input())
for _ in range(T):
    N, M, u, v = map(int, input().split())
    adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)

    reachable_from_u = bfs(u, -1, adj, N)
    if not reachable_from_u[v]:
        print(0)
        continue

    count = 0

    for x in range(1, N + 1):
        if x == u or x == v:  
            continue

        if not reachable_from_u[x]:
            continue
        reachable_from_x = bfs(x, -1, adj, N)
        if not reachable_from_x[v]:
            continue

        reachable_without_x = bfs(u, x, adj, N)
        if not reachable_without_x[v]:
            count += 1

    print(count)
