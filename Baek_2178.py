import sys

n, m = map(int, sys.stdin.readline().split())
a = [[0]*m for i in range(n)]
h = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(n):
    b = (sys.stdin.readline().rstrip())
    for j in range(m):
        if b[j] == "1":
            a[i][j] = 1


#b = []
c = []
f = 1
c.append((0,0))
c.append("o")

while c:
    d = c[0]
    del c[0]
    if d == "o":
        c.append("o")
        f += 1
        d = c[0]
        del c[0]
    for x, y in h:
        if 0 <= int(d[0])+x < n and 0 <= int(d[1])+y < m and a[int(d[0])+x][int(d[1])+y] == 1:
            if d[0]+x == n-1 and d[1]+y == m-1:
                print(f+1)
                exit()
            c.append((d[0]+x, d[1]+y))
            a[int(d[0])+x][int(d[1])+y] = 0
    a[int(d[0])][int(d[1])] = 0