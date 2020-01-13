import sys

n = int(sys.stdin.readline())
st = []
an = []

for i in range(n):
    st.append(int(sys.stdin.readline()))

an.append(st[0])
an.append(st[1]+st[0])
an.append(max(st[2]+an[0], st[2]+st[1]))

for i in range(3, n):
    an.append(max(st[i]+an[i-2], st[i]+st[i-1]+an[i-3]))

print(an[-1])