t = int(input().strip())
for _ in range(t):
    s = input().strip()
    k = input().strip()
    cnt, i = 0, 0
    while i <= len(s) - len(k):
        if s[i:i + len(k)] == k:
            cnt += 1
            i += len(k)
        else: i += 1
    
    print(cnt)