import sys

n = int(input())

for i in range(n):
    a = []
    c = []
    b = int(sys.stdin.readline())
    for j in range(b):
        d = list(sys.stdin.readline().split())
        if d[1] not in a:
            a.append(d[1])
            c.append(1)
        else:
            c[a.index(d[1])] += 1
    e = 1

    for i in c:
        e *= (i+1)
    print(e-1)