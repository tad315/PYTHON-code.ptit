emails = set()
with open('CONTACT.in', 'r') as f:
    for line in f:
        email = line.strip().lower()
        if email:
            emails.add(email)
for e in sorted(emails):
    print(e)
            