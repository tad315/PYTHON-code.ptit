def generate(n):
    d = ['0', '2', '4', '6', '8']
    res = []
    
    for l in range(2, len(str(n)) + 1, 2):
        halfL = l // 2
        
        def Try(cur):
            if len(cur) == halfL:
                tmp = cur + cur[::-1]
                num = int(tmp)
                if num < n:
                    res.append(num)
                return
            
            for i in d:
                if len(cur) == 0 and i == '0':
                    continue
                Try(cur + i)
        Try('')
    return sorted(res)

t = int(input())
for _ in range(t):
    n = int(input())
    ans = generate(n)
    print(" ".join(map(str, ans)))
                
