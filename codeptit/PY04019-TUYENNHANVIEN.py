class ThiSinh:
    def __init__(self, name, id, avg):
        self.id = id
        self.name = name
        self.avg = avg
        if avg < 5: self.rank = "TRUOT"
        elif avg < 8: self.rank = "CAN NHAC"
        elif avg <= 9.5: self.rank = "DAT"
        else: self.rank = "XUAT SAC"
        
def cmp(x):
    return (x.avg * (-1))

if __name__ == "__main__":
    n = int(input())
    ds = []
    for i in range(n):
        name = input()
        lt = float(input())
        th = float(input())
        if lt > 10: lt /= 10.0
        if th > 10: th /= 10.0
        avg = (lt + th) / 2.0
        id = ""
        id += "TS0" + str(i + 1)
        ds.append(ThiSinh(name, id, avg))
    ds.sort(key = cmp)
    for x in ds:
        print(x.id + ' ' + x.name + ' ' + '{:.2f}'.format(x.avg) + ' ' + x.rank)