from collections import Counter
s = input()
nums = []
for i in range(0, len(s) - 1, 2):
    tmp = int(s[i : i + 2])
    nums.append(tmp)
for x, c in Counter(nums).items():
    print(f'{x} {c}')