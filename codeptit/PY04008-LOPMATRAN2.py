import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    t = next(it)
    out_lines = []
    for _ in range(t):
        n = next(it); m = next(it)
        a = [[next(it) for _ in range(m)] for _ in range(n)]
        res = [[0]*n for _ in range(n)]
        for i in range(n):
            ai = a[i]
            for j in range(n):
                aj = a[j]
                s = 0
                for k in range(m):
                    s += ai[k] * aj[k]
                res[i][j] = s
        for row in res:
            out_lines.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
