class HoaDon:
    def __init__(self, ma, ten, sl, gia, ck):
        self.ma = ma.strip()
        self.ten = ten.strip()
        self.sl = int(sl)
        self.gia = int(gia)
        self.ck = int(ck)
        self.tong_tien = self.sl * self.gia - self.ck
    def __str__(self):
        return f"{self.ma} {self.ten} {self.sl} {self.gia} {self.ck} {self.tong_tien}"
def main():
    n = int(input())
    ds = []
    for _ in range(n):
        ma = input().strip()
        ten = input().strip()
        sl = input().strip()
        gia = input().strip()
        ck = input().strip()
        ds.append(HoaDon(ma, ten, sl, gia, ck))
    
    ds.sort(key=lambda x: -x.tong_tien)
    
    for hd in ds: print(hd)
if __name__ == "__main__":
    main()
        