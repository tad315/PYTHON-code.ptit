def chuan_hoa(ten):
    parts = ten.strip().split()
    return " ".join(w.capitalize() for w in parts)

class Team:
    _id = 1
    def __init__(self, ten_team, truong):
        self.ma = f"Team{Team._id:02d}"
        Team._id += 1
        self.ten_team = ten_team.strip()
        self.truong = truong.strip()
class ThiSinh:
    _id = 1
    def __init__(self, ten, ma_team, teams):
        self.ma = f"C{ThiSinh._id:03d}"
        ThiSinh._id += 1
        self.ten = chuan_hoa(ten)
        self.team = teams[ma_team].ten_team
        self.truong = teams[ma_team].truong
    def __str__(self):
        return f"{self.ma} {self.ten} {self.team} {self.truong}"
    
n = int(input().strip())
teams = {}
for _ in range(n):
    ten_team = input().strip()
    truong = input().strip()
    t = Team(ten_team, truong)    
    teams[t.ma] = t
m = int(input().strip())
ds = []
for _ in range(m):
    ten = input().strip()
    ma_team = input().strip()
    ds.append(ThiSinh(ten, ma_team, teams))
ds.sort(key=lambda x: x.ten)
for ts in ds:
    print(ts)