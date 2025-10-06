t = int(input())
for _ in range(t):
    s = input().strip()
    a = s[:2]
    b = s[-2:]
    if a == b:
        print ('YES')
    else: 
        print('NO')
