from collections import defaultdict, deque

class Logic:
    def __init__ (self):
        self.graph = defaultdict(list)
        self.indeg = defaultdict(int)
        self.members = set()
        
    def add_comparison(self, a, op, b):
        self.members.update([a, b])
        if op == '>':
            self.graph[a].append(b)
            self.indeg[b] += 1
        elif op == '<':
            self.graph[b].append(a)
            self.indeg[a] += 1
    def is_possible(self):
        for name in self.members:
            self.indeg.setdefault(name, 0)
        q = deque([x for x in self.indeg if self.indeg[x] == 0])
        cnt = 0
        while q: 
            u = q.popleft()
            cnt += 1
            for v in self.graph[u]:
                self.indeg[v] -= 1
                if self.indeg[v] == 0:
                    q.append(v)
        return cnt == len(self.members)
    
n = int(input())
logic = Logic()
for _ in range(n):
    a, op, b = input().split()
    logic.add_comparison(a, op, b)
print('possible' if logic.is_possible() else 'imppossible')