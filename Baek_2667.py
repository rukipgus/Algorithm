import sys

n = int(sys.stdin.readline())
a = []
an = []

for i in range(n):
    f = sys.stdin.readline()
    for j in range(len(f)):
        if f[j] == "1":
            a.append((i,j))

while a:
    b = []
    c = []
    c.append(a[0])
    del a[0]

    while c:
        d = c[0]
        del c[0]
        b.append(d)

        if (d[0]+1,d[1]) in a:
            c.append((d[0]+1,d[1]))
            a.remove((d[0]+1,d[1]))
        if (d[0]-1,d[1]) in a:
            c.append((d[0]-1,d[1]))
            a.remove((d[0]-1,d[1]))
        if (d[0],d[1]+1) in a:
            c.append((d[0],d[1]+1))
            a.remove((d[0],d[1]+1))
        if (d[0],d[1]-1) in a:
            c.append((d[0],d[1]-1))
            a.remove((d[0],d[1]-1))
    an.append(len(b))

an.sort()
print(len(an))
for i in range(len(an)):
    print(an[i])