def get_band(d):
    if 39 <= d <= 40: return 9.0
    elif 37 <= d <= 38: return 8.5
    elif 35 <= d <= 36: return 8.0
    elif 33 <= d <= 34: return 7.5
    elif 30 <= d <= 32: return 7.0
    elif 27 <= d <= 29: return 6.5
    elif 23 <= d <= 26: return 6.0
    elif 20 <= d <= 22: return 5.5
    elif 16 <= d <= 19: return 5.0
    elif 13 <= d <= 15: return 4.5
    elif 10 <= d <= 12: return 4.0
    elif 7 <= d <= 9: return 3.5
    elif 5 <= d <= 6: return 3.0
    elif 3 <= d <= 4: return 2.5
    return 0.0

def round_ielts(x):
    frac = x - int(x)
    if frac < 0.25:
        return float(int(x))
    elif frac < 0.75:
        return int(x) + 0.5
    else:
        return float(int(x) + 1)
    
for _ in range(int(input())):
    r, l, s, w = input().split()
    r, l = int(r), int(l)
    s, w = float(s), float(w)
    avg = (get_band(r) + get_band(l) + s + w) / 4
    print(round_ielts(avg))