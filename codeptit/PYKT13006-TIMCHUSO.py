import sys
input = sys.stdin.readline

MOD = 1000

def mat_mul(a, b):
    # nhân 2 ma trận 2x2 modulo MOD
    return [
        [(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD,
         (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD],
        [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD,
         (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD],
    ]

def mat_pow(n):
    # tính M^(n) với M = [[6, -4], [1, 0]] (mod 1000)
    M = [[6, MOD - 4], [1, 0]]  # -4 ≡ 996 (mod 1000)
    res = [[1, 0], [0, 1]]      # ma trận đơn vị
    while n > 0:
        if n & 1:
            res = mat_mul(res, M)
        M = mat_mul(M, M)
        n >>= 1
    return res

def last3_digits(n):
    # trả về 3 chữ số cuối của floor((3+sqrt(5))^n)
    if n == 0:
        return 1  # (3+sqrt5)^0 = 1 -> 001
    if n == 1:
        return 5  # (3+sqrt5)^1 ≈ 5.236 -> floor = 5 -> 005 (mod 1000 = 5)

    # S0 = 2, S1 = 6, S_n = 6 S_{n-1} - 4 S_{n-2}
    P = mat_pow(n - 1)   # M^(n-1)
    S1, S0 = 6, 2
    Sn = (P[0][0] * S1 + P[0][1] * S0) % MOD  # lấy phần tử S_n
    return (Sn - 1) % MOD   # floor(A_n) = S_n - 1

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    out_lines = []
    for case in range(1, T + 1):
        n = int(next(it))
        val = last3_digits(n)
        out_lines.append(f"Case #{case}: {val:03d}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
