class Customer:
    def __init__(self, id, name, oIdx, nIdx):
        self.id = 'KH{:02}'.format(id)
        self.name = name
        self.oIdx = oIdx
        self.nIdx = nIdx

    def calc(self):
        self.total = self.nIdx - self.oIdx
        if self.total <= 50:
            self.price = self.total * 102
        elif self.total <= 100:
            self.price = round(self.total * 150 * 1.03 - 2575)
        else:
            self.price = self.total * 210 - 7875
            
    def __str__(self):
        return f"{self.id} {self.name} {int(self.price)}"

n = int(input())
customers = []

for i in range(1, n + 1):
    name = input()
    oIdx = int(input())
    nIdx = int(input())
    customer = Customer(i, name, oIdx, nIdx)
    customer.calc()
    customers.append(customer)

customers.sort(key=lambda x: x.price, reverse=True)

for customer in customers:
    print(customer)    
        