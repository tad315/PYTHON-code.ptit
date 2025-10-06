def getSum(s):
    sum = 0
    for i in s:
        sum += int(i)
    return sum

t = int(input())
for _ in range(t):
    n = input()
    if getSum(n) % 3 == 0:
        print("YES")
    else: 
        print("NO")