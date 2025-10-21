unit_price = {}
def init():
    unit_price[('Xe_con', '5')] = 10000
    unit_price[('Xe_con', '7')] = 15000
    unit_price[('Xe_tai', '2')] = 20000
    unit_price[('Xe_khach', '29')] = 50000
    unit_price[('Xe_khach', '45')] = 70000
    
init()

class Car:
    def __init__(self, plate, loai, ghe, tt, ngay):
        self.plate = plate
        self.loai = loai
        self.ghe = ghe
        self.tt = tt
        self.ngay = ngay
cars = []
profit = {}

n = int(input())
for _ in range(n):
    car = input().split()
    cars.append(Car(*car))
for c in cars:
    if c.tt == 'IN':
        if c.ngay not in profit:
            profit[c.ngay] = unit_price[(c.loai, c.ghe)]
        else:
            profit[c.ngay] += unit_price[(c.loai, c.ghe)]
for d, p in profit.items():
    print(f"{d}: {p}")
    