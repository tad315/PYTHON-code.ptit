import sys
input = sys.stdin.readline

MOD = 10**9 + 7
MAXN = 100000

# Precompute factorials
fact = [1] * (MAXN + 1)
invfact = [1] * (MAXN + 1)

for i in range(1, MAXN + 1):
    fact[i] = fact[i-1] * i % MOD

invfact[MAXN] = pow(fact[MAXN], MOD-2, MOD)
for i in range(MAXN, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD

def C(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    return fact[n] * invfact[k] % MOD * invfact[n-k] % MOD


# ===== Main =====

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0

for i in range(N):
    ai = A[i]
    # i is 1-based in formula → convert
    left = C(i, K-1)          # C(i-1, K-1) but index shift: A[i] is A_(i+1)
    right = C(N-i-1, K-1)     # C(N-i, K-1)

    ans = (ans + ai * (left - right)) % MOD

print(ans % MOD)
