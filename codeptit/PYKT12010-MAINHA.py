import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    A = list(map(int, input().split()))

    ans = 10**30

    for i in range(n):
        Ci = [A[j] + abs(i - j) for j in range(n)]
        Ci.sort()

        med = Ci[n//2]
        
        Hmin = max(i, n - 1 - i) + 1
        H = med if med >= Hmin else Hmin
        
        s = 0
        for x in Ci:
            if x >= H:
                s += x - H
            else:
                s += H - x

        if s < ans:
            ans = s

    print(ans)

solve()
