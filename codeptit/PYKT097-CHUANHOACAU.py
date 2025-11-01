lines = []
while True:
    try:
        line = input()
        if not line:
            break
        lines.append(line.strip().capitalize())        
    except EOFError:
        break
for line in lines:
    p = " ".join(line.split())
    p = p.replace(' .', '.').replace(' !', '!').replace(' ?', '?')
    if not p.endswith(('.', '!', '?')):
        p += '.'
    print(p)