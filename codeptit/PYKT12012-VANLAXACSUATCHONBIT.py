import sys
import math

input = sys.stdin.readline

def sum_popcount_upto(n: int) -> int:
    """Tổng số bit 1 của tất cả số trong [0..n]"""
    if n < 0:
        return 0
    res = 0
    k = 0
    while (1 << k) <= n:
        cycle = 1 << (k + 1)
        full = (n + 1) // cycle
        res += full * (1 << k)
        rem = (n + 1) % cycle
        if rem > (1 << k):
            res += rem - (1 << k)
        k += 1
    return res

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    if A > B:
        A, B = B, A

    total_numbers = B - A + 1
    expected_sum = 0.0

    maxL = B.bit_length()  # độ dài nhị phân lớn nhất

    for L in range(1, maxL + 1):
        low = max(A, 1 << (L - 1))
        high = min(B, (1 << L) - 1)
        if low > high:
            continue

        sum_pop = sum_popcount_upto(high) - sum_popcount_upto(low - 1)
        expected_sum += sum_pop / L

    prob = expected_sum / total_numbers
    # cộng một chút để tránh lỗi làm tròn kiểu 0.611109 -> 0.61110
    print(f"{prob + 1e-12:.5f}")
