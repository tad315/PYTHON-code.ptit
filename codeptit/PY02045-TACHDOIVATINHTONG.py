s = input()
while len(s) > 1:
    mid = len(s) // 2
    tmp = int(s[:mid]) + int(s[mid:])
    print(tmp)
    s = str(tmp)
    