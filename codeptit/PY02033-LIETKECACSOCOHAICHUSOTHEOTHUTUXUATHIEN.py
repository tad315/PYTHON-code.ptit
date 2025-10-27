s = input()
nums = []
for i in range(0, len(s) - 1, 2):
    tmp = int(s[i : i + 2])
    if tmp not in nums:
        nums.append(tmp)
print(*nums)