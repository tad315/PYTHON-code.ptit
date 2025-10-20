import math 
for _ in range(int(input())):
    s = input()
    s1 = s[::-1]
    if math.gcd(int(s), int(s1)) == 1: print("YES") 
    else: print("NO")