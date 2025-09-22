def getMul(s):
    mul = 1
    for i in s:
        if i != '0':
            mul *= int(i)
    return mul

for _ in range(int(input())):
    n = input()
    print(getMul(n))
    