def find_char(n, k):
    mid = 1 << (n - 1)
    if k == mid: return chr(64 + n)
    elif k < mid: return find_char(n - 1, k)
    return find_char(n - 1, k - mid)

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(find_char(n, k))