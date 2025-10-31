from datetime import datetime

DIST = 120  
START = datetime.strptime("6:00", "%H:%M")

class CuaRo:
    def __init__(self, ten, dv, time_str):
        self.ten = ten.strip()
        self.dv = dv.strip()
        self.time_str = time_str.strip()

        end = datetime.strptime(self.time_str, "%H:%M")
        self.elapsed_sec = (end - START).seconds
        hours = self.elapsed_sec / 3600.0
        self.vt = int(DIST / hours + 0.5)

        self.ma = self._tao_ma()

    def _tao_ma(self):
        p1 = ''.join(w[0].upper() for w in self.dv.split())
        p2 = ''.join(w[0].upper() for w in self.ten.split())
        return p1 + p2

    def __str__(self):
        return f"{self.ma} {self.ten} {self.dv} {self.vt} Km/h"

def main():
    n = int(input().strip())
    ds = []
    for _ in range(n):
        ten = input().strip()
        dv = input().strip()
        tg = input().strip()
        ds.append(CuaRo(ten, dv, tg))

    ds.sort(key=lambda x: x.elapsed_sec)

    for cr in ds:
        print(cr)

if __name__ == "__main__":
    main()
