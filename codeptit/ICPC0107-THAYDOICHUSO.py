def solve():
    for _ in range (int(input())):
        p, q = input().split()
        data = input().split()
        if len(data) == 1:
            x1 = data[0]
            x2 = input()
        else:
            x1, x2 = data
        x1 = x1.replace(p, q)
        x2 = x2.replace(p, q)
        num1 = int(x1) + int(x2)
        x1 = x1.replace(q, p)
        x2 = x2.replace(q, p)
        num2 = int(x1) + int(x2)
        print(min(num1, num2), max(num1, num2))

if __name__ == "__main__":
    solve()