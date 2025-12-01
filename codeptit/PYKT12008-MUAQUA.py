import sys
input = sys.stdin.readline

class BIT:
    def __init__(self, n):
        self.n = n
        self.cnt = [0] * (n + 2)
        self.s = [0] * (n + 2)

    def update(self, i, dc, ds):
        n = self.n
        while i <= n:
            self.cnt[i] += dc
            self.s[i] += ds
            i += i & -i

    def prefix_count(self, i):
        res = 0
        while i > 0:
            res += self.cnt[i]
            i -= i & -i
        return res

    def prefix_sum(self, i):
        res = 0
        while i > 0:
            res += self.s[i]
            i -= i & -i
        return res

    def kth(self, k):
        pos = 0
        bit_mask = 1 << (self.n.bit_length()) 
        while bit_mask:
            nxt = pos + bit_mask
            if nxt <= self.n and self.cnt[nxt] < k:
                k -= self.cnt[nxt]
                pos = nxt
            bit_mask >>= 1
        return pos + 1


def read_like_list():
    while True:
        line = input().split()
        if line:
            break
    A = int(line[0])
    arr = list(map(int, line[1:]))
    while len(arr) < A:
        arr.extend(map(int, input().split()))
    return A, arr


def main():
    N, M, K = map(int, input().split())
    costs = list(map(int, input().split()))

    A, x_list = read_like_list()
    B, y_list = read_like_list()

    likeA = [False] * N
    likeB = [False] * N

    for idx in x_list:
        likeA[idx - 1] = True
    for idx in y_list:
        likeB[idx - 1] = True

    both = []
    onlyA = []
    onlyB = []
    none = []

    for i in range(N):
        c = costs[i]
        if likeA[i] and likeB[i]:
            both.append((c, i))
        elif likeA[i]:
            onlyA.append((c, i))
        elif likeB[i]:
            onlyB.append((c, i))
        else:
            none.append((c, i))
            
    if N < M:
        print(-1)
        return

    if len(both) + len(onlyA) < K or len(both) + len(onlyB) < K:
        print(-1)
        return

    both.sort()
    onlyA.sort()
    onlyB.sort()
    none.sort()

    tStart = max(0, K - len(onlyA), K - len(onlyB))
    tEnd = min(K, len(both))
    if tStart > tEnd:
        print(-1)
        return
  
    all_ids = list(range(N))
    all_ids.sort(key=lambda i: costs[i])
    pos = [0] * N 
    for i, gid in enumerate(all_ids):
        pos[gid] = i + 1

    bit = BIT(N)

    is_forced = [False] * N

    needA = K - tStart
    needB = K - tStart

    forced_sum = 0
    forced_count = 0

    both_ids = [idx for _, idx in both]
    onlyA_ids = [idx for _, idx in onlyA]
    onlyB_ids = [idx for _, idx in onlyB]
    none_ids = [idx for _, idx in none]

    for i in range(tStart):
        gid = both_ids[i]
        is_forced[gid] = True
        forced_sum += costs[gid]
        forced_count += 1

    for i in range(needA):
        gid = onlyA_ids[i]
        is_forced[gid] = True
        forced_sum += costs[gid]
        forced_count += 1

    for i in range(needB):
        gid = onlyB_ids[i]
        is_forced[gid] = True
        forced_sum += costs[gid]
        forced_count += 1
        
    for gid in range(N):
        if not is_forced[gid]:
            bit.update(pos[gid], 1, costs[gid])

    INF = 10**30
    ans = INF

    t = tStart
    while t <= tEnd:
        forced_count = (t) + max(0, K - t) + max(0, K - t)

        if forced_count <= M:
            rem = M - forced_count
            if rem == 0:
                ans = min(ans, forced_sum)
            else:
                total_pool = bit.prefix_count(N)
                if total_pool >= rem:
                    pos_k = bit.kth(rem)
                    extra_sum = bit.prefix_sum(pos_k)
                    ans = min(ans, forced_sum + extra_sum)

        if t == tEnd:
            break

        gid_both = both_ids[t]
        bit.update(pos[gid_both], -1, -costs[gid_both])
        is_forced[gid_both] = True
        forced_sum += costs[gid_both]

        if K - t > 0:
            idxA = K - t - 1 
            gid_A = onlyA_ids[idxA]
            is_forced[gid_A] = False
            forced_sum -= costs[gid_A]
            bit.update(pos[gid_A], 1, costs[gid_A])
            
        if K - t > 0:
            idxB = K - t - 1
            gid_B = onlyB_ids[idxB]
            is_forced[gid_B] = False
            forced_sum -= costs[gid_B]
            bit.update(pos[gid_B], 1, costs[gid_B])

        t += 1

    print(ans if ans < INF else -1)


if __name__ == "__main__":
    main()
