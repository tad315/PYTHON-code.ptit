def toMinutes(s : str) -> int:
    hh, mm = map(int, s.split(':'))
    return hh * 60 + mm

class Gamer:
    def __init__ (self, id, name, inT, outT):
        self.id = id
        self.name = name
        self.m = toMinutes(outT) - toMinutes(inT)
    def __str__(self):
        hh = self.m // 60
        mm = self.m % 60
        return f"{self.id} {self.name} {hh} gio {mm} phut"
if __name__ == "__main__":
    n = int(input())
    ds = []
    for i in range(1, n + 1):
        id = input()
        name = input()
        inT = input()
        outT = input()
        ds.append(Gamer(id, name, inT, outT))
    ds.sort(key = lambda x: -x.m)
    for i in ds:
        print(i)