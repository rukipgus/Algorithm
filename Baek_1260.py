import sys

n, m, v = map(int, sys.stdin.readline().split())
c = [[0]*(n+1) for i in range(n+1)]
df = []
bf = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    c[a][b] += 1
    c[b][a] += 1

d = []
e = [v]

while e:
    u = e[0]
    del e[0]

    if u not in d:
        d.append(u)
        for i in range(1,n+1):
            if c[u][i] > 0:
                if i not in d and i not in e:
                    e.append(i)

#print(d)

h = []
e = [v]

while e:
    u = e[0]
    del e[0]
    if u not in h:
        h.append(u)
    k = []
    for i in range(1,n+1):
        if c[u][i] > 0:
            if i not in h:
                k.append(i)
    k.extend(e)
    e = k

for i in h:
    print(i, end = " ")
print()

for i in d:
    print(i, end = " ")