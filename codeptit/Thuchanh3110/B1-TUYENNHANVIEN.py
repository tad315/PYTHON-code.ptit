class NhanVien:
    def __init__ (self, id, name, avg):
        self.id = id
        self.name = name
        self.avg = avg
        if avg < 5: self.rank = 'TRUOT'
        elif avg < 8: self.rank = 'CAN NHAC'
        elif avg <= 9.5: self.rank = 'DAT'
        else: self.rank = 'XUAT SAC'
        
n = int(input())
ds = []
for i in range(n):
    name = input().strip()
    lt = float(input().strip())
    th = float(input().strip())
    if lt > 10: lt /= 10.0
    if th > 10: th /= 10.0
    avg = (lt + th) / 2.0
    id = f'TS0{i + 1}'
    ds.append(NhanVien(id, name, avg))
ds.sort(key=lambda x: -x.avg)
for nv in ds:
    print(f'{nv.id} {nv.name} {nv.avg:.2f} {nv.rank}')