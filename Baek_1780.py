import sys

n = int(sys.stdin.readline())
p =[]

for i in range(n):
    p.append(list(sys.stdin.readline().rstrip()))

def nt(x,y,z):
    a = False
    b = False
    c = False
    d = 0
    for i in range(y, y+z):
        for j in range(x, x+z):
            if p[i][j] == -1:
                a = True
                d
            elif p[i][j] == 0:
                b = True