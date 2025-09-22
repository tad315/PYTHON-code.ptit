def cnt4(n):
    cnt = 0
    while n > 0:
        if n % 10 == 4:
            cnt += 1
        n //= 10
    return cnt

def cnt7(n):
    cnt = 0
    while n > 0:
        if n % 10 == 7:
            cnt += 1
        n //= 10
    return cnt

n = int(input())
if cnt4(n) + cnt7(n) == 4 or cnt4(n) + cnt7(n) == 7:
    print("YES")
else: 
    print('NO')
