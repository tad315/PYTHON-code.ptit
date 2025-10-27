from collections import deque

def check(s):
    return s.count('2') > len(s) / 2

def gen(n):
    res = []
    q = deque(['0', '1', '2'])
    while len(res) < n:
        s = q.popleft()
        if s[0] != '0' and check(s): res.append(s)
        for c in '012':
            q.append(s + c)
    return res
for _ in range(int(input())):
    n = int(input())
    print(*gen(n))