import sys
import math

MOD = 10**9 + 7

def sieve(n):
    isPrime = [True] * (n + 1)
    isPrime[0 : 2] = [False, False]
    for p in range(2, int(n ** 0.5) + 1):
        if isPrime[p]:
            step = p
            start = p * p
            isPrime[start : n + 1 : step] = [False] * (((n - start) // step) + 1)
    return [i for i, v in enumerate(isPrime) if v]

def cntPair(a, b, primes):
    ans = 1
    a1 = a - 1
    for p in primes:
        if p > b: break
        e = 0
        pp = p
        while pp <= b:
            e += b // pp - (a1 // pp)
            pp *= p
        ans = (ans * (2 * e + 1)) % MOD
    return ans

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    t = data[0]
    pairs = data[1:]
    tests = [(pairs[i], pairs[i + 1]) for i in range(0, 2 * t, 2)]
    max_b = max(b for _, b in tests)
    primes = sieve(max_b)
    out = []
    for a, b in tests:
        out.append(str(cntPair(a, b, primes)))
    print("\n".join(out))

if __name__ == "__main__":
    main()