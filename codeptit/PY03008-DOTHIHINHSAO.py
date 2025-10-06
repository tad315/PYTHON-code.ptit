n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
cnt = 0
for u in adj:
    cnt += (len(u) > 1)
if cnt == 1: print("Yes")
else: print("No")