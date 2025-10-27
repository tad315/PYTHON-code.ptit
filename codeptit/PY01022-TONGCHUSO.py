s = input()
cnt, sum = 0, 100
while sum >= 10:
    sum = 0
    for c in s:
        sum += ord(c) - 48
    cnt += 1
    s = str(sum)
print(cnt)