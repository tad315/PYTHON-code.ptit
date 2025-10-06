from decimal import Decimal, ROUND_HALF_UP

class HS:
    def __init__(self, idx, name, scores):
        self.idx = f"HS{idx:02d}"
        self.name = name.strip()
        self.scores = scores  
        self.avg = self.tinhDTB()
        self.rank = self.xepLoai()

    def tinhDTB(self):
        total = self.scores[0] * 2 + self.scores[1] * 2 + sum(self.scores[2:])
        return total / Decimal(12) 

    def xepLoai(self):
        if self.avg >= Decimal('9'): return "XUAT SAC"
        elif self.avg >= Decimal('8'): return "GIOI"
        elif self.avg >= Decimal('7'): return "KHA"
        elif self.avg >= Decimal('5'): return "TB"
        else: return "YEU"

    def __str__(self):
        avg_disp = self.avg.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        return f"{self.idx} {self.name} {avg_disp} {self.rank}"

if __name__ == "__main__":
    n = int(input().strip())
    ds = []
    for i in range(1, n + 1):
        name = input().strip()
        scores = [Decimal(x) for x in input().split()]
        ds.append(HS(i, name, scores))

    ds.sort(key=lambda x: (-x.avg, x.idx))

    for hs in ds:
        print(hs)
