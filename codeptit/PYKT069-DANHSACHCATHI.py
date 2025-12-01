from datetime import datetime

class CaThi:
    _id = 1
    def __init__(self, ngay, gio, phong):
        self.ma = f"C{CaThi._id:03d}"
        CaThi._id += 1
        self.ngay = datetime.strptime(ngay.strip(), "%d/%m/%Y")
        self.gio = datetime.strptime(gio.strip(), "%H:%M")
        self.phong = phong.strip()
    def __str__(self):
        return f"{self.ma} {self.ngay.strftime('%d/%m/%Y')} {self.gio.strftime('%H:%M')} {self.phong}"

with open("CATHI.in", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

n = int(lines[0])
ds = []
i = 1
for _ in range(n):
    ngay = lines[i]; gio = lines[i+1]; phong = lines[i+2]
    ds.append(CaThi(ngay, gio, phong))
    i += 3

ds.sort(key=lambda x: (x.ngay, x.gio, x.ma))

for ca in ds:
    print(ca)
