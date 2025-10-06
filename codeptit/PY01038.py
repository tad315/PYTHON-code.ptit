#Kiểm tra chia hết cho 7
import sys

def reverse(x : int) -> int:
    return int(str(x)[::-1])

input = sys.stdin.readline
out = []

t = int(input())
for _ in range(t):
    n = int(input())
    ans = -1
    for _ in range(1000):
        if n % 7 == 0:
            ans = n
            break
        n = n + reverse(n)
    out.append(str(ans))
sys.stdout.write("\n".join(out))