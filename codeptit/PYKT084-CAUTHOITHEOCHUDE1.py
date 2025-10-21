n = int(input().strip())
lines = [input().rstrip() for _ in range(n)]

topics = []
counts = {}
current_topic = None

for line in lines:
    if line == "": 
        current_topic = None
        continue
    if current_topic is None:
        current_topic = line
        topics.append(line)
        counts[current_topic] = 0
    else:
        counts[current_topic] += 1

for t in topics:
    print(f"{t}: {counts[t]}")
