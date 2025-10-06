while True:
    n = int(input())
    if not n: break
    a = [int(input()) for _ in range(n)] 
    if (min(a) == max(a)): print("BANG NHAU")
    else:
        print(min(a), max(a))