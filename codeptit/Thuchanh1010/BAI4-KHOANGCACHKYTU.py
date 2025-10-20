def check(s, s1):
    for i in range(len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s1[i]) - ord(s1[i - 1])): return "NO"  
    return "YES"

for _ in range(int(input())):
    s = input()
    s1 = s[::-1]
    print(check(s, s1))
    
        