t = int(input())
for _ in range(t):
    s = input().strip()
    res = ""
    for i in range(0, len(s), 2):
        c = s[i]
        cnt = int(s[i + 1])
        res += c * cnt
    print (res)
  
