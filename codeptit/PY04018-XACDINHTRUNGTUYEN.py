class GiaoVien:
    ut = {'1' : 2.0, '2': 1.5, '3': 1.0, '4': 0.0}
    mh = {'A': 'TOAN', 'B': 'LY', 'C':'HOA'}
    
    def __init__(self, ma, ten, ma_xt, tin, cm):
        self.ma = f"GV{ma:02d}"
        self.ten = ten
        self.ma_xt = ma_xt
        self.tin = float(tin)
        self.cm = float(cm)
        self.mon = GiaoVien.mh[self.ma_xt[0]]
        self.diem_ut = GiaoVien.ut[self.ma_xt[1]]
        self.tong = self.tin * 2 + self.cm + self.diem_ut
        self.kq = 'TRUNG TUYEN' if self.tong >= 18 else 'LOAI'
        
    def __str__(self):
        return f'{self.ma} {self.ten} {self.mon} {self.tong:.1f} {self.kq}'

n = int(input())
ds = []
for i in range(1, n + 1):
    ten = input().strip()
    ma_xt = input().strip()
    tin = input().strip()
    cm = input().strip()
    ds.append(GiaoVien(i, ten, ma_xt, tin, cm))
ds.sort(key=lambda x: -x.tong)
for gv in ds:
    print(gv)