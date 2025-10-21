n = int(input().strip())
lines = [input().strip() for _ in range(n)]
cnt = [len(line.split()) for line in lines]

kinds = []
i = 0
while i < n:
    if i + 3 < n and all(cnt[i + k] == 7 for k in range(4)):
        kinds.append(2)
        i += 4
    else:
        pairs = 0
        while i + 1 < n and cnt[i] == 6 and cnt[i + 1] == 8:
            i += 2
            pairs += 1
            if i + 3 < n and all(cnt[i + k] == 7 for k in range(4)):
                break
        if pairs == 0:
            if i + 3 < n and all(cnt[i + k] == 7 for k in range(4)):
                kinds.append(2)
                i += 4
            else: 
                kinds.append(1)
                i += 2 if i + 1 < n else 1
        else: 
            kinds.append(1)
print(len(kinds))
for k in kinds:
    print(k)