import sys
input = sys.stdin.readline

def solve():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        U = float(input().strip())
        P = list(map(float, input().split()))
        
        P.sort()
        P.append(1.0)
        
        for i in range(n):
            if U <= 0:
                break
            current = P[i]
            next_level = min(P[i + 1], 1.0)
            if next_level <= current:
                continue
            
            need = (next_level - current) * (i + 1)
            if need <= U + 1e-12: 
                for j in range(i + 1):
                    P[j] = next_level
                U -= need
            else:
                delta = U / (i + 1)
                for j in range(i + 1):
                    P[j] += delta
                U = 0
                break
        
        P = P[:n]
 
        prod = 1.0
        for x in P:
            prod *= x
        
        print(f"{prod:.6f}")

if __name__ == "__main__":
    solve()
