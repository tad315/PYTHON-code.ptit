from datetime import datetime

class MonHoc:
    def __init__(self, ma, ten):
        self.ma = ma.strip()
        self.ten = ten.strip()
class LichThi:
    _id = 1
    def __init__ (self, mon, ngay, gio, nhom, ds_mon):
        self.ma = f'T{LichThi._id:03d}'
        LichThi._id += 1
        self.mon = next(mh for mh in ds_mon if mh.ma == mon)
        self.ngay = datetime.strptime(ngay.strip(), "%d/%m/%Y")
        self.gio = datetime.strptime(gio.strip(), "%H:%M")
        self.nhom = nhom.strip()
        
    def __str__(self):
        return f"{self.ma} {self.mon.ma} {self.mon.ten} {self.ngay.strftime('%d/%m/%Y')} {self.gio.strftime('%H:%M')} {self.nhom}"
    
n, m = map(int, input().split())
ds_mon = []
for _ in range(n):
    ma = input().strip()
    ten = input().strip()
    ds_mon.append(MonHoc(ma, ten))
ds_ca = []
for _ in range(m):
    mon, ngay, gio, nhom = input().split()
    ds_ca.append(LichThi(mon, ngay, gio, nhom, ds_mon))
    
ds_ca.sort(key=lambda x: (x.ngay, x.gio, x.mon.ma))
for ca in ds_ca:
    print(ca)