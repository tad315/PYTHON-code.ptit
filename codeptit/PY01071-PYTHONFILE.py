s = input().strip()
if len(s) >= 3 and s[-3:].lower() == ".py":
    print("yes")
else:
    print("no")
