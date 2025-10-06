class Complex:
    def __init__ (self, r, i):
        self.r = r
        self.i = i
    def __add__ (self, other):
        return Complex(self.r + other.r, self.i + other.i)
    def __mul__ (self, other):
        return Complex(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)
    def __str__ (self):
        if self.i >= 0:
            return f"{self.r} + {self.i}i"
        else:
            return f"{self.r} - {-self.i}i"
        
if __name__ == '__main__':
    for _ in range(int(input())):
        a, b, c, d = map(int, input().split())
        f1 = Complex(a, b)
        f2 = Complex(c, d)
        S = f1 + f2
        C = S * f1
        D = S * S
        print(f"{C}, {D}")
        