class ThiSinh:
    def __init__(self, hoTen, ngaySinh, d1, d2, d3):
        self.hoTen = hoTen.strip()
        self.ngaySinh = ngaySinh.strip()
        self.d1 = float(d1)
        self.d2 = float(d2)
        self.d3 = float(d3)
        self.sum = self.d1 + self.d2 + self.d3
    def __str__(self):
        return f"{self.hoTen} {self.ngaySinh} {self.sum:.1f}"
if __name__ == "__main__":
    hoTen = input().strip()
    ngaySinh = input().strip()
    d1 = input().strip()
    d2 = input().strip()
    d3 = input().strip()
    ts = ThiSinh(hoTen, ngaySinh, d1, d2, d3)
    print(ts)