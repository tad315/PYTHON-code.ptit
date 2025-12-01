class MonThi:
    def __init__ (self, ma, ten, hinh_thuc):
        self.ma = ma
        self.ten = ten
        self.hinh_thuc = hinh_thuc
    def __str__(self):
        return f"{self.ma} {self.ten} {self.hinh_thuc}"
n = int(input().strip())
ds = []
for _ in range(n):
    ma = input().strip()
    ten = input().strip()
    hinh_thuc = input().strip()
    ds.append(MonThi(ma, ten, hinh_thuc))
ds.sort(key=lambda x: x.ma)
for mon in ds:
    print(mon)