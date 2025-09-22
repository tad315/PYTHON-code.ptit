def change(n, b, X):
    if b == 2: return X
    elif b == 4:
        if n == 0: return '0'
        digits = []
        while n > 0:
            digits.append(str(n % 4))
            n //= 4
        return "".join(reversed(digits))
    elif b == 8:
        return oct(n)[2:]
    elif b == 16:
        return hex(n)[2:].upper()

for _ in range(int(input().strip())):
    b = int(input().strip())
    X = input().strip()
    if b == 2: 
        print(X)
    else:
        n = int(X, 2)
        print(change(n, b, X))
