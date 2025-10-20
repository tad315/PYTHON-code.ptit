def min_steps(strings):
    n = len(strings)
    L = len(strings[0])
    ans = float('inf')
    for target in strings:
        total_moves = 0
        ok = True
        for s in strings:
            cnt = s + s
            pos = cnt.find(target)
            if pos == -1 or pos >= L:
                ok = False
                break
            total_moves += pos
        if ok:
            ans = min(ans, total_moves)
    return -1 if ans == float('inf') else ans

if __name__ == "__main__":
    n = int(input().strip())
    strings = [input().strip() for _ in range(n)]
    print(min_steps(strings))
        