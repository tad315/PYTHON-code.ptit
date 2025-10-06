from itertools import combinations

n, k = map(int, input().split())
a = list(map(int, input().split()))
vals = sorted(set(a))
for c in combinations(vals, k):
    print(" ".join(map(str, c)))