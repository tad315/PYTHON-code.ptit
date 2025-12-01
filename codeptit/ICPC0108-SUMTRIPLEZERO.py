import sys
input = sys.stdin.readline

def cnt_triplets(a):
    a.sort()
    n = len(a)
    cnt = 0
    for i in range(0, n - 2):
        l, r =  i + 1, n - 1
        while l < r:
            s = a[i] + a[l] + a[r]
            if s == 0:
                cnt += 1
                l += 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return cnt

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(cnt_triplets(a))