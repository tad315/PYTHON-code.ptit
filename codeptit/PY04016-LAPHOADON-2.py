from datetime import datetime
class KhachHang:
    def __init__(self, ma, ten, so_phong, nhan, tra, dv):
        self.ma = f"KH{ma:02d}"
        self.ten = ten.strip()
        self.so_phong = so_phong.strip()
        self.nhan = datetime.strptime(nhan.strip(), "%d/%m/%Y")
        self.tra = datetime.strptime(tra.strip(), "%d/%m/%Y")
        self.dv = int(dv)
        self.so_ngay = (self.tra - self.nhan).days + 1
        self.tang = int(self.so_phong[0])
        self.don_gia = self.tinh_don_gia()
        self.thanh_tien = self.so_ngay * self.don_gia + self.dv
    
    def tinh_don_gia(self):
        if self.tang == 1: return 25
        elif self.tang == 2: return 34
        elif self.tang == 3: return 50
        else: return 80
        
    def __str__(self):
        return f"{self.ma} {self.ten} {self.so_phong} {self.so_ngay} {self.thanh_tien}"
    
def main():
    n = int(input())
    ds = []
    for i in range(n):
        ten = input().strip()
        so_phong = input().strip()
        nhan = input().strip()
        tra = input().strip()
        dv = input().strip()
        ds.append(KhachHang(i + 1, ten, so_phong, nhan, tra, dv))
    ds.sort(key=lambda x: -x.thanh_tien)
    for kh in ds:
        print(kh)
if __name__ == "__main__":
    main()
