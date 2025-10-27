s = input()
nums = set()
for i in range(0, len(s) - 1, 2):
    tmp = int(s[i : i + 2])
    nums.add(tmp)
print(*sorted(nums))