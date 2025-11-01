def chuan_hoa(ten):
    parts = ten.strip().split()
    return " ".join(part.capitalize() for part in parts)

class ThiSinh:
    _id = 1
    def __init__(self, ten, diem, dt, kv):
        self.ma = f"TS{ThiSinh._id:02d}"
        ThiSinh._id += 1
        self.ten = chuan_hoa(ten)
        self.diem = diem
        self.dt = dt
        self.kv = kv
        self.tong_diem = self.tinh_tong_diem()
        if self.tong_diem >= 20.5: self.kq = "Do"
        else: self.kq = "Truot"
    def tinh_tong_diem(self):
        res = self.diem
        if self.kv == 1: res += 1.5
        elif self.kv == 2: res += 1.0
        
        if self.dt != "Kinh": res += 1.5
        return res
    def __str__(self):
        return f"{self.ma} {self.ten} {self.tong_diem:.1f} {self.kq}"
    
n = int(input())
ds = []
for _ in range(n):
    ten = input().strip()
    diem = float(input().strip())
    dt = input().strip()
    kv = int(input().strip())
    ds.append(ThiSinh(ten, diem, dt, kv))
ds.sort(key=lambda x: (-x.tong_diem, x.ma))
for ts in ds:
    print(ts)
        
