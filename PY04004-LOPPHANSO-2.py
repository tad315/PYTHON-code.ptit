import math

class PS:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutGon(self):
        g = math.gcd(self.tu, self.mau)
        self.tu //= g
        self.mau //= g
        return self
    
    def add(self, other):
        a, b = self.tu, self.mau
        c, d = other.tu, other.mau
        tu1 = a * d + c * b
        mau1 = d * b
        return (PS(tu1, mau1)).rutGon()
    
    def __str__(self):
        return f"{self.tu}/{self.mau}"
    
if __name__ == '__main__':
    a, b, c, d = map(int, input().split())
    f1 = PS(a, b).rutGon()
    f2 = PS(c, d).rutGon()
    f = f1.add(f2)
    print(f)
