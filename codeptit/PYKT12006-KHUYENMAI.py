import sys

input = sys.stdin.readline

def solve_one():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cost = sum(b)

    deltas = [a[i] - b[i] for i in range(n)]
    deltas.sort()

    for i in range(n):
        if i < k or deltas[i] < 0:
            cost += deltas[i]
        else:
            break

    print(cost)
    
solve_one()

