import sys
input = sys.stdin.readline

MOD = 10**9 + 7

def mod_pow(a, b, mod=MOD):
    res = 1
    a %= mod
    while b:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res

def solve_one(n, K):
    m = K + 2  # số điểm dùng để nội suy

    # Tính y[i] = S(i) = 1^K + ... + i^K, i = 1..m
    y = [0] * (m + 1)
    s = 0
    for i in range(1, m + 1):
        s = (s + mod_pow(i, K)) % MOD
        y[i] = s

    if n <= m:
        return y[n]

    # factorial
    fact = [1] * (m + 1)
    for i in range(1, m + 1):
        fact[i] = fact[i-1] * i % MOD

    # prefix & suffix tích (n - j)
    pre = [1] * (m + 2)
    for i in range(1, m + 1):
        pre[i] = pre[i-1] * (n - i) % MOD

    suf = [1] * (m + 3)
    for i in range(m, 0, -1):
        suf[i] = suf[i+1] * (n - i) % MOD

    ans = 0
    for i in range(1, m + 1):
        # tử số: ∏_{j≠i} (n - j)
        num = pre[i-1] * suf[i+1] % MOD

        # mẫu số: (i-1)! * (-1)^{m-i} * (m-i)!
        den = fact[i-1] * fact[m-i] % MOD
        if (m - i) & 1:     # nếu m-i lẻ → nhân thêm -1
            den = (-den) % MOD

        term = y[i] * num % MOD * mod_pow(den, MOD - 2) % MOD
        ans = (ans + term) % MOD

    return ans

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    out_lines = []
    for _ in range(T):
        n = int(next(it))
        K = int(next(it))
        out_lines.append(str(solve_one(n, K)))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
