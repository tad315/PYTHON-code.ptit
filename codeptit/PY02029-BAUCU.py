from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = Counter(a)
if len(cnt) < 2: print('NONE')
else:
    sorted_cnt = sorted(cnt.values(), reverse=True)
    first = sorted_cnt[0]
    second = None
    for x in sorted_cnt:
        if x < first:
            second = x
            break
    if second is None: print('NONE')
    else: 
        res = [k for k, v in cnt.items() if v == second]
        print(min(res))