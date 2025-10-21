def valid_ipv4(ip: str) -> bool:
    parts = ip.split(".")
    if len(parts) != 4: return False
    for p in parts:
        if not p.isdigit(): return False
        if len(p) > 1 and p[0] == '0': return False
        val = int(p)
        if not (0 <= val <= 255): return False
    return True

for _ in range(int(input())):
    s = input().strip()
    print('YES' if valid_ipv4(s) else 'NO')