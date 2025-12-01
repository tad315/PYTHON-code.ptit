from datetime import datetime

monhoc = {}
with open("MONTHI.in") as f:
    n = int(f.readline().strip())
    for _ in range(n):
        ma = f.readline().strip()
        ten = f.readline().strip()
        hinh_thuc = f.readline().strip()     # không dùng
        monhoc[ma] = ten

cathi = {}
with open("CATHI.in") as f:
    m = int(f.readline().strip())
    for i in range(1, m + 1):
        ngay = f.readline().strip()
        gio = f.readline().strip()
        phong = f.readline().strip()
        ma_ca = f"C{i:03d}"  
        cathi[ma_ca] = (ngay, gio, phong)

lich = []
with open("LICHTHI.in") as f:
    k = int(f.readline().strip())
    for _ in range(k):
        ma_ca, ma_mon, nhom, so_sv = f.readline().split()
        ngay, gio, phong = cathi[ma_ca]
        ten_mon = monhoc[ma_mon]

        obj = {
            "ma_ca": ma_ca,
            "ngay": ngay,
            "gio": gio,
            "phong": phong,
            "ten_mon": ten_mon,
            "nhom": nhom,
            "so_sv": so_sv
        }
        lich.append(obj)

def to_datetime(d, h):
    return datetime.strptime(d + " " + h, "%d/%m/%Y %H:%M")

lich.sort(key=lambda x: (to_datetime(x["ngay"], x["gio"]), x["ma_ca"]))

for x in lich:
    print(x["ngay"], x["gio"], x["phong"], x["ten_mon"], x["nhom"], x["so_sv"])
