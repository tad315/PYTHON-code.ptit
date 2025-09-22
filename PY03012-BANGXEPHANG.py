n = int(input().strip())
st = []
for _ in range(n):
    name = input().strip()
    c, t = map(int, input().split())
    st.append((name, c, t))
st.sort(key=lambda x: (-x[1], x[2], x[0]))

for s in st:
    print(s[0], s[1], s[2])