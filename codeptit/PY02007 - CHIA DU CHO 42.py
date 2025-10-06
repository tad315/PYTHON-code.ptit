def cnt42 (list):
    res = {i % 42 for i in list}
    return len(res)

a = []
while (len(a) < 10):
    line = input()
    num = list(map(int, line.split()))
    a.extend(num[:10 - len(a)])
print(cnt42(a))

