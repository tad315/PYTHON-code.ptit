def getSum(s):
    sum = 0
    for i in range(1, len(s), 2):
        sum += int(s[i])
    return sum

def getMul(s):
    mul = 1
    for i in range(0, len(s), 2):
        if s[i] != '0': mul *= int(s[i])
    return mul

for _ in range(int(input())):
    n = input()
    print(getMul(n), getSum(n))