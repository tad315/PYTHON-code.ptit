n = int(input())
a = []
while len(a) < n:
    a.extend(map(int, input().split()))

even = sorted([x for x in a if x % 2 == 0])
odd = sorted([x for x in a if x % 2 != 0], reverse=True)

res = []
i, j = 0, 0

for x in a:
    if x % 2 == 0:
        res.append(even[i])
        i += 1
    else:
        res.append(odd[j])
        j += 1
print(*res)