class HS:
    _id = 1
    def __init__(self, name, t, v, a, l, h, s, su, d, gd, cn):
        self.id = f"HS{HS._id:02d}"
        HS._id += 1
        self.name = name
        self.t = float(t)
        self.v = float(v)
        self.a = float(a)
        self.l = float(l)
        self.h = float(h)
        self.s = float(s)
        self.su = float(su)
        self.d = float(d)
        self.gd = float(gd)
        self.cn = float(cn)
        self.total = (self.t * 2 + self.v * 2 + self.a + self.l + self.h + self.s + self.su + self.d + self.gd + self.cn) / 12.0
        self.total = round(self.total + 1e-8, 1)
        if self.total >= 9.0: self.rank = "XUAT SAC"
        elif self.total >= 8.0: self.rank = "GIOI"
        elif self.total >= 7.0: self.rank = "KHA"
        elif self.total >= 5.0: self.rank = "TB"
        else: self.rank = "YEU"
    def __str__(self):
        return f"{self.id} {self.name} {self.total:.1f} {self.rank}"

n = int(input())
ds = []
for _ in range(n):
    name = input().strip()
    t, v, a, l, h, s, su, d, gd, cn = map(float, input().strip().split())
    hs = HS(name, t, v, a, l, h, s, su, d, gd, cn)
    ds.append(hs)
ds.sort(key=lambda x: -x.total)
for hs in ds:
    print(hs)
    