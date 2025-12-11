import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    prefix_max = [0] * n
    suffix_min = [0] * n

    prefix_max[0] = arr[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i-1], arr[i])

    suffix_min[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        suffix_min[i] = min(suffix_min[i+1], arr[i])

    ans = 0
    for i in range(n):
        left_ok = prefix_max[i] <= arr[i]
        right_ok = True if i == n-1 else arr[i] < suffix_min[i+1]
        if left_ok and right_ok:
            ans += 1

    print(ans)
