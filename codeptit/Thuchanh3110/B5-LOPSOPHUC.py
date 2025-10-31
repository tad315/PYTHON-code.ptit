class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    def __add__(self, o):
        return Complex(self.r + o.r, self.i + o.i)
    def __mul__(self, o):
        return Complex(self.r * o.r - self.i * o.i, self.r * o.i + self.i * o.r)
    def __str__(self):
        if self.i >= 0:
            return f"{self.r} + {self.i}i"
        return f"{self.r} - {-self.i}i"
n = int(input())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    z1 = Complex(a, b)
    z2 = Complex(c, d)
    S = z1 + z2
    C = S * z1
    D = S * S
    print(f"{C}, {D}")