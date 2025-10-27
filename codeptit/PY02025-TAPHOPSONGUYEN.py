n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A = set(a)
B = set(b)

giao = sorted(A & B)
a_sub_b = sorted(A - B)
b_sub_a = sorted(B - A)

print(*giao)
print(*a_sub_b)
print(*b_sub_a)
