from datetime import datetime
class TheLoai:
    _id = 1
    def __init__(self, ten):
        self.ma = f'TL{TheLoai._id:03d}'
        TheLoai._id += 1
        self.ten = ten.strip()

class Phim:
    _id = 1
    def __init__(self, ma_tl, ngay, ten, so_tap, ds_tl):
        self.ma = f'P{Phim._id:03d}'
        Phim._id += 1
        self.theloai = next(tl for tl in ds_tl if tl.ma == ma_tl)
        self.ngay = datetime.strptime(ngay.strip(), '%d/%m/%Y')
        self.ten = ten.strip()
        self.so_tap = int(so_tap)
    def __str__(self):
        return f'{self.ma} {self.theloai.ten} {self.ngay.strftime("%d/%m/%Y")} {self.ten} {self.so_tap}'
    
n, m = map(int, input().split())
ds_tl = [TheLoai(input()) for _ in range(n)]
ds_phim = []
for _ in range(m):
    ma_tl = input().strip()
    ngay = input().strip()
    ten = input().strip()
    so_tap = input().strip()
    ds_phim.append(Phim(ma_tl, ngay, ten, so_tap, ds_tl))
ds_phim.sort(key=lambda x: (x.ngay, x.ten.lower(), -x.so_tap))
for p in ds_phim:
    print(p)