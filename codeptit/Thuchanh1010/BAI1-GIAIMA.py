for _ in range (int(input())):
    s = input()
    for j in s:
        if j.isalpha(): tmp = j
        elif j.isdigit():
            for i in range(int(j)): print(tmp, end='')
    print()
    