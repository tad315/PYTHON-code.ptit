from itertools import permutations

s = input().strip()
for p in permutations(s):
    print("".join(p))