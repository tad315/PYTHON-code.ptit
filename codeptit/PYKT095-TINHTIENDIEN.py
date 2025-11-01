def chuan_hoa(ten):
    parts = ten.strip().split()
    return " ".join(w.capitalize() for w in parts)

class KhachHang:
    _id = 1
    def __init__(self, ten, loai, dau, cuoi):
        self.ma = f"KH{KhachHang._id:02d}"
        KhachHang._id += 1
        self.ten = chuan_hoa(ten)
        self.loai = loai
        self.dau = int(dau)
        self.cuoi = int(cuoi)
        self.so = self.cuoi - self.dau
        self.dinh_muc = self.get_dinh_muc()
        self.tien_trong, self.tien_vuot, self.vat, self.tong = self.tinh_tien()
    def get_dinh_muc(self):
        if self.loai == 'A': return 100
        elif self.loai == 'B': return 500
        elif self.loai == 'C': return 200
        else: return 0
    def tinh_tien(self):
        if self.so < self.dinh_muc:
            tien_trong = self.so * 450
            tien_vuot = 0
        else: 
            tien_trong = self.dinh_muc * 450
            tien_vuot = (self.so - self.dinh_muc) * 1000
        vat = tien_vuot // 20
        tong = tien_trong + tien_vuot + vat
        return tien_trong, tien_vuot, vat, tong
    def __str__(self):
        return f"{self.ma} {self.ten} {self.tien_trong} {self.tien_vuot} {self.vat} {self.tong}"
            
n = int(input())
ds = []
for _ in range(n):
    ten = input()
    loai, dau, cuoi = input().strip().split()
    ds.append(KhachHang(ten, loai, dau, cuoi))
ds.sort(key=lambda x: -x.tong)
for kh in ds:
    print(kh)