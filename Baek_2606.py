import sys

n = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = [[i] for i in range(1, n+1)]


for i in range(a):
    c, d = map(int, sys.stdin.readline().split())
    e = 0
    f = 0

    for j in range(len(b)):
        if c in b[j]:
            e = j
        if d in b[j]:
            f = j
        
    b[e].extend(b[f])
    b[e]=list(set(b[e]))

    if e != f:
        del b[f]

for i in range(len(b)):
    if 1 in b[i]:
        print(len(b[i])-1)
        break