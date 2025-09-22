def snt(n):
    if n < 2: return False
    if n == 2: return True
    elif n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
cnt = {}
order = []
for x in a:
    if snt(x):
        if x not in cnt:
            cnt[x] = 1
            order.append(x)
        else:
            cnt[x] += 1
for x in order:
    print(x, cnt[x])