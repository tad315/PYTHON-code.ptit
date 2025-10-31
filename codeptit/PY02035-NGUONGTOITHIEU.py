from collections import Counter
s = input()
k = int(input())
nums = []
for i in range(0, len(s) - 1, 2):
    tmp = int(s[i : i + 2])
    nums.append(tmp)
ok = False
nums.sort()
for x, c in Counter(nums).items():
    if c >= k:
        print(f'{x} {c}')
        ok = True
if not ok: print('NOT FOUND')