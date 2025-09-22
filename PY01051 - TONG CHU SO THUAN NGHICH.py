def getSum(s):
    sum = 0
    for ch in s:
        sum += int(ch)
    return sum

for _ in range(int(input())):
    s = input().strip()
    n = str(getSum(s))
    if n == n[::-1] and len(n) > 1: print("YES")
    else: print("NO")