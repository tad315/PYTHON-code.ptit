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
    def __str__(self):
        return f"{self.tu}/{self.mau}"
if __name__ == '__main__':
    a, b = map(int, input().split())
    f = PS(a, b).rutGon()
    print(f)
