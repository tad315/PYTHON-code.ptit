from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = Counter(a)
    res = []
    for num, freq in cnt.items():
        if freq > n // 2:
            res.append(num)
    if res:
        print(min(res))
    else:
        print('NO')