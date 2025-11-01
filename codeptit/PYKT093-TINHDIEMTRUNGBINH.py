def chuan_hoa(ten):
    parts = ten.strip().split()
    return " ".join(part.capitalize() for part in parts)

class SinhVien:
    _id = 1
    def __init__(self, ten, d1, d2, d3):
        self.ma = f"SV{SinhVien._id:02d}"
        SinhVien._id += 1
        self.ten = chuan_hoa(ten)
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.dtb = self.tinh_tb(d1, d2, d3)
        self.rank = 0
    def tinh_tb(self, d1, d2, d3):
        return round((d1 * 3 + d2 * 3 + d3 * 2) / 8 + 1e-8, 2)
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.dtb:.2f} {self.rank}"

n = int(input())
ds = []
for _ in range(n):
    ten = input().strip()
    d1 = float(input().strip())
    d2 = float(input().strip())
    d3 = float(input().strip())
    ds.append(SinhVien(ten, d1, d2, d3))
ds.sort(key=lambda x: (-x.dtb, x.ma))
rank = 1
ds[0].rank = 1
for i in range(1, n):
    if ds[i].dtb == ds[i-1].dtb:
        ds[i].rank = ds[i-1].rank
    else:
        ds[i].rank = i + 1
for sv in ds: 
    print(sv)
    



