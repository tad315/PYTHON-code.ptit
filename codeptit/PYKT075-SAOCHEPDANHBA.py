with open('SOTAY.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

contacts = []
ngay = ''

i = 0
while i < len(lines):
    line = lines[i]
    if line.startswith("Ngay "):                 
        ngay = line.split(" ", 1)[1]            
        i += 1
    else:
        ten = lines[i]
        sdt = lines[i + 1]
        contacts.append((ten, sdt, ngay))
        i += 2

def sort_key(contact):
    parts = contact[0].split()
    return (parts[-1], " ".join(parts[:-1]))

contacts.sort(key=sort_key)

with open('DIENTHOAI.txt', 'w') as f:
    for ten, sdt, ngay in contacts:
        f.write(f"{ten}: {sdt} {ngay}\n")
