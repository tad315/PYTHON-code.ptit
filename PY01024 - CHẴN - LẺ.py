t = int(input())
for _ in range (t):
    s = input().strip()
    Sum = sum(int (c) for c in s)
    dk1 = Sum % 10 == 0
    dk2 = all(abs(int(s[i]) - int(s[i - 1])) == 2 for i in range (1, len(s)))
    if dk1 and dk2:
        print('YES')
    else:
        print('NO')
