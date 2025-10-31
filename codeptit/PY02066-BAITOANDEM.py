n = int(input())
a = []
while len(a) < n:
    a.extend(list(map(int, input().split())))
ok = False
for i in range(1, max(a) + 1):
    if i not in a:
        print(i)
        ok = True
if not ok: 
    print("Excellent!")
        