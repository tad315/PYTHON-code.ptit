class Matrix:
    def __init__(self, n, m, data):
        self.n = n
        self.m = m
        self.data = data
    
    def calc(self):
        res = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                s = 0
                for k in range(self.m):
                    s += self.data[i][k] * self.data[j][k]
                res[i][j] = s
        return res

if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().split())
        data = []
        for _ in range(n):
            row = list(map(int, input().split()))
            data.append(row)
        mt = Matrix(n, m, data)
        res = mt.calc()
        for row in res: 
            print(" ".join(map(str, row)))