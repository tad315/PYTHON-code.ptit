import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

all_vals = set()
cur = set()

for x in a:
    newcur = {x}  
    for v in cur:
        newcur.add(v | x)
    cur = newcur
    all_vals |= cur  

print(len(all_vals))
