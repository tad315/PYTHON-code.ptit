s1 = input().rstrip()
s2 = input().rstrip()
p = int(input().strip())
res = s1[:p-1] + s2 + s1[p-1:]
print(res)