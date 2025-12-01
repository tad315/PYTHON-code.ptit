import sys
import bisect
input = sys.stdin.readline

def can(G, k, arr, prefix, N):
    # tìm số lượng phần tử <= G
    idx = bisect.bisect_right(arr, G)
    # tổng min(ai, G)
    total = prefix[idx] + (N - idx) * G
    return total >= G * k

T = int(input())
for _ in range(T):
    N, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + arr[i]

    left, right = 0, sum(arr) // k
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if can(mid, k, arr, prefix, N):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    print(ans)
