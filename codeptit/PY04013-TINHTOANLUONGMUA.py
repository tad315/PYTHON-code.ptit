class Station:
    def __init__(self, name):
        self.name = name
        self.totalRain = 0.0
        self.totalMinutes = 0
    def addRecord(self, s, e, rain):
        sMin = self.to_minutes(s)
        eMin = self.to_minutes(e)
        time = eMin - sMin
        self.totalRain += rain
        self.totalMinutes += time
    def calc(self):
        if self.totalMinutes == 0: return 0.0
        return self.totalRain / self.totalMinutes * 60
    @staticmethod
    def to_minutes(time_str):
        hh, mm = map(int, time_str.split(":"))
        return hh * 60 + mm

if __name__ == "__main__":
    n = int(input().strip())
    stations = {}
    order = []
    for _ in range(n):
        name = input().strip()
        s = input().strip()
        e = input().strip()
        rain = float(input().strip())
        if name not in stations:
            stations[name] = Station(name)
            order.append(name)
        stations[name].addRecord(s, e, rain)
    for idx, name in enumerate(order, start = 1):
        st = stations[name]
        print(f"T{idx:02d} {st.name} {st.calc():.2f}")