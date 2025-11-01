class NhanVien:
    def __init__(self, ma, ten, luongcb, cong, ban):
        self.ma = ma.strip()
        self.ten = ten.strip()
        self.luongcb = int(luongcb)
        self.cong = int(cong)
        self.ban = ban
        self.hs = self.tinh_heso()
        self.luong = self.luongcb * self.cong * self.hs * 1000
    def tinh_heso(self):
        nhom = self.ma[0]
        nam = int(self.ma[1:3])
        if nhom == 'A':
            if nam <= 3: return 10
            elif nam <= 8: return 12
            elif nam <= 15: return 14
            else: return 20
        elif nhom == 'B':
            if nam <= 3: return 10
            elif nam <= 8: return 11
            elif nam <= 15: return 13
            else: return 16
        elif nhom == 'C':
            if nam <= 3: return 9
            elif nam <= 8: return 10
            elif nam <= 15: return 12
            else: return 14
        elif nhom == 'D':
            if nam <= 3: return 8
            elif nam <= 8: return 9
            elif nam <= 15: return 11
            else: return 13
        return 0
    def __str__(self):
        return f"{self.ma} {self.ten} {self.ban} {self.luong}"
    
n = int(input().strip())
phong_ban = {}
for _ in range(n):
    parts = input().strip().split(maxsplit=1)
    ma_pb, ten_pb = parts[0], parts[1]
    phong_ban[ma_pb] = ten_pb

m = int(input().strip())
ds = []
for _ in range(m):
    ma = input().strip()
    ten = input().strip()
    luong_cb = input().strip()
    ngay_cong = input().strip()
    ma_pb = ma[-2:]
    nv = NhanVien(ma, ten, luong_cb, ngay_cong, phong_ban[ma_pb])
    ds.append(nv)

for nv in ds:
    print(nv)







        