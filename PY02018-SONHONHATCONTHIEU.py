n =  int(input())
a = list(map(int, input().split()))
dd = [False] * (n + 2)
for i in a:
    if 1 <= i <= n + 1:
        dd[i] = True
for i in range(1, n + 2):
    if not dd[i]:
        print(i)
        break