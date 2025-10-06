n = int(input())
a = list(map(int, input().split()))
minStep = float('inf')
bestVal = None
for val in a:
    step = sum(abs(x - val) for x in a)
    if step < minStep:
        minStep = step
        bestVal = val
print(minStep, bestVal)