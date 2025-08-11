s = input().strip()
n = len(s)
H = 0
h = 0
for i in range(n):
    if s[i].isupper():
        H += 1
    else: 
        h += 1
if H > h: 
    print(s.upper())
else: 
    print(s.lower())
    
