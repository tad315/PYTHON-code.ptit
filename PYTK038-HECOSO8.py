def change(n, b):
    return oct(n)[2:]

n = input()
print(change(int(n, 2), 8))