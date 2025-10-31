from itertools import permutations
import math

for _ in range(int(input())):
    n = int(input())
    arr = list(range(1, n + 1))
    
    perms = list(permutations(arr))
    
    perms.sort(reverse=True)
    
    print(math.factorial(n))

    print(" ".join("".join(map(str, p)) for p in perms))