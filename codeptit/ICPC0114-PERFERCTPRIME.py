def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def reverse_number(n):
    return int(str(n)[::-1])
for _ in range(int(input())):
    n = int(input())
    if snt(n) and snt(reverse_number(n)):
        print("Yes")
    else: print("No")