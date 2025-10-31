def toMinutes(s):
    h, m = map(int, s.split(':'))
    return h * 60 + m

class Gamer:
    def __init__(self, id, name, inT, outT):
        self.id = id
        self.name = name
        self.m = toMinutes(outT) - toMinutes(inT)
    def __str__(self):
        hh = self.m // 60
        mm = self.m % 60
        return f'{self.id} {self.name} {hh} gio {mm} phut'
    
n = int(input())
ds = []
for _ in range(n):
    id = input().strip()
    name = input().strip()
    inT = input().strip()
    outT = input().strip()
    ds.append(Gamer(id, name, inT, outT))
ds.sort(key=lambda x: -x.m)
for x in ds:
    print(x)