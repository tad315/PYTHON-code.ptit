n = int(input())
a = list(map(float, input().split()))

sum = 0.0
cnt = 0
for i in a:
    if i != min(a) and i != max(a):
        sum += i
        cnt += 1
print(f"{(sum / cnt):.2f}")