from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = Counter(a)
    for x in a:
        if freq[x] & 1:
            print(x)
            break