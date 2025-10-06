def solve(d, m):
    if (m == 3 and d >= 21) or (m == 4 and d <= 19): return "Bach Duong" 
    elif (m == 4 and d >= 20) or (m == 5 and d <= 20): return "Kim Nguu" 
    elif (m == 5 and d >= 21) or (m == 6 and d <= 20): return "Song Tu"
    elif (m == 6 and d >= 21) or (m == 7 and d <= 22): return "Cu Giai"
    elif (m == 7 and d >= 23) or (m == 8 and d <= 22): return "Su Tu"
    elif (m == 8 and d >= 23) or (m == 9 and d <= 22): return "Xu Nu"
    elif (m == 9 and d >= 23) or (m == 10 and d <= 22): return "Thien Binh"
    elif (m == 10 and d >= 23) or (m == 11 and d <= 22): return "Thien Yet"
    elif (m == 11 and d >= 23) or (m == 12 and d <= 21): return "Nhan Ma"
    elif (m == 12 and d >= 22) or (m == 1 and d <= 19): return "Ma Ket"
    elif (m == 1 and d >= 20) or (m == 2 and d <= 18): return "Bao Binh"
    elif (m == 2 and d >= 19) or (m == 3 and d <= 20): return "Song Ngu"

for _ in range(int(input())):
    d, m = map(int, input().split())
    print(solve(d, m))