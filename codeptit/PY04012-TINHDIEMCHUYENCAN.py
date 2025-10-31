class SinhVien:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.dd = ""
        self.diem = 10
        self.note = ""
        
    def tinh_diem(self):
        v = self.dd.count('v')
        m = self.dd.count('m')
        self.diem = 10 - (2 * v + 1 * m)
        if self.diem < 0:
            self.diem = 0
        if self.diem == 0:
            self.note = 'KDDK'
    def __str__(self):
        if self.note:
            return f"{self.ma} {self.ten} {self.lop} {self.diem} {self.note}"
        return f"{self.ma} {self.ten} {self.lop} {self.diem}"

def main():
    n = int(input().strip())
    ds = []
    for _ in range(n):
        ma = input().strip()
        ten = input().strip()
        lop = input().strip()
        ds.append(SinhVien(ma, ten, lop))
    for _ in range(n):
        line = input().strip().split()
        ma, dd = line[0], line[1]
        for sv in ds:
            if sv.ma == ma:
                sv.dd = dd
                sv.tinh_diem()
                break
    for sv in ds: print(sv)

if __name__ == "__main__":
    main()
        