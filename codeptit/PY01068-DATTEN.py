from itertools import combinations

n, k = map(int, input().split())
names = sorted(set(input().split()))

for c in combinations(names, k):
    print(*c)
