import sys

a = int(sys.stdin.readline())

for i in range(a):
    b = int(sys.stdin.readline())
    c = int(sys.stdin.readline())
    apt = [[0]*c for k in range(b+1)]
    for x in range(c):
        apt[0][x]=x+1
    for x in range(b+1):
        apt[x][0]=1
    for y in range(1,b+1):
        for x in range(1,c):
            apt[y][x] = (apt[y-1][x]+apt[y][x-1])
    print(apt[b][c-1])